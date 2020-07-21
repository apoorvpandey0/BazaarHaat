from uuid import uuid4

from django.db import models
from users.models import Profile
from product.models import Product
from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
ORDER_STATUS=((0,'Processing'),
              (1,'Packed by the seller'),
              (2,'Picked up from seller'),
              (3,'Out for delivery'),
              (4,'Reviewed'),
              (5,'Delivered'),
              (6,'On Hold')
             )
P_CHOICES=((1,'Credit/Debit Card'),
           (2,'Net Banking'),
           (3,'Cash On Delivery'),
          )

class Cart(models.Model):
    """docstring for Cart."""
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return "Cart -> "+self.user.user.get_full_name()

class CartItem(models.Model):
    id = models.UUIDField(
                primary_key = True,
                default = uuid4,
                editable = False)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(
                default=1,
                validators=[MaxValueValidator(5), MinValueValidator(1)]
                )
    TAX_AMOUNT = 19.25

    def citem_price(self):
        return self.product.my_price*self.quantity

    def __str__(self):
        return  self.cart.user.user.get_full_name() + " -> " + str(self.product)

class WishListItem(models.Model):
    id = models.UUIDField(
                primary_key = True,
                default = uuid4,
                editable = False)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(
                default=1,
                validators=[MaxValueValidator(5), MinValueValidator(1)]
                )
    def __str__(self):
        return  self.cart.user.user.get_full_name() + " -> " + str(self.product)

class Order(models.Model):
    id= models.UUIDField(
                primary_key = True,
                default = uuid4,
                editable = False)
    cart    = models.ForeignKey(Cart,on_delete=models.DO_NOTHING)
    datetime= models.DateTimeField(default=datetime.now)
    status  = models.IntegerField(choices=ORDER_STATUS,default=0)
    total   = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    method  = models.IntegerField(choices=P_CHOICES,default=3)

    def __str__(self):
        return "Order -> "+self.cart.user.user.get_full_name()

    def calc_total(self):
        TAX=0
        CI=CartItem.objects.filter(cart=self.cart)
        sum=0
        for item in CI:
            sum+=item.product.my_price
        self.total=sum+TAX

class Coupon(models.Model):
    id= models.UUIDField(
                primary_key = True,
                default = uuid4,
                editable = False)
    title = models.CharField(
                max_length = 20,
                default = "Haha",
                unique = True,
                help_text="Title of the Coupon",)
    limit = models.IntegerField(
                default = 50,
                help_text = "Maximum limit to the number of coupons",
                )
    used  = models.IntegerField(
                default = 0,
                help_text = "This many coupons are used")
