from PIL import Image
from uuid import uuid4
import markdown as m

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe

from shop.models import Shop
from users.models import Profile
from pages.models import Category,SubCategory
from taggit.managers import TaggableManager

from django.utils.translation import ugettext_lazy as _
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

class Product(models.Model):
    id = models.UUIDField(
                primary_key = True,
                default = uuid4,
                editable = False)
    title       = models.CharField(
                            max_length=50,
                            blank=False,
                            default="Mast cheez")
    description = models.TextField(
                            blank=False,
                            default="This product is cool!")
    actual_price= models.DecimalField(
                            decimal_places=2,
                            max_digits=10,
                            blank=False,
                            default=100)
    my_price    = models.DecimalField(
                            decimal_places=2,
                            max_digits=10,
                            blank=False,
                            default=80)
    image       = models.ImageField(upload_to='products')
    tags = TaggableManager(through=UUIDTaggedItem)
    date_created= models.DateTimeField(default=timezone.now)
    summary     = models.TextField(
                            blank=False,
                            default="I love this product")
    shop        = models.ForeignKey(
                            Shop,
                            on_delete=models.CASCADE,
                            null=True,
                            help_text=_("The shop which is going to sell this product."))
    seller      = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    # shop_name   = models.CharField(max_length=50,blank=False,help_text=_(" Ex: Manohar-MP Nagar"))
    stock       = models.IntegerField(blank=False,default=0,help_text=_("Quantity of product you have in stock.Ex: 150"))
    approved    = models.BooleanField(default=False)
    is_service  = models.BooleanField(default=False)
    category    = models.ForeignKey(
                        Category,
                        on_delete=models.SET_NULL,null=True,
                        help_text=_("Category the product belongs to")
    )

    subcategory = models.ForeignKey(
                        SubCategory,
                        on_delete=models.SET_NULL,null=True,
                        help_text=_("Sub category the product belongs to")
    )

    def __str__(self):
        return self.title

    #This will redirect to post detail view after creating a new post
    def get_absolute_url(self):
        return reverse('users-profile')

    def create_tags(self):
        tags = title.split()
        self.tags = tags

    def get_markdown(self):
        #I dont understand when to use this
        title = self.title
        markdown_text = m.markdown(title)
        return mark_safe(markdown_text)

    def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height>500 or img.width >500 :
            output_size=(500,500)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # def get_cat_list(self):
    #     k = self.category # for now ignore this instance method
    #
    #     breadcrumb = ["dummy"]
    #     while k is not None:
    #         breadcrumb.append(k.slug)
    #         k = k.parent
    #     for i in range(len(breadcrumb)-1):
    #         breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
    #     return breadcrumb[-1:0:-1]
class Review(models.Model):
    id = models.UUIDField(
                primary_key = True,
                default = uuid4,
                editable = False)
    product = models.ForeignKey(Product,on_delete = models.SET_NULL,null = True)
    user = models.ForeignKey(Profile,on_delete = models.CASCADE,null = True)
    text = models.CharField(max_length = 500)
    created = models.DateTimeField(default=timezone.now,editable = False)
    rating = models.IntegerField(default = 0,validators=[MinValueValidator(0),MaxValueValidator(5)])

    class Meta:
        ordering = ['user']
