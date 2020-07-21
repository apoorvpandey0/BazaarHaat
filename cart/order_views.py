from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (DetailView, ListView, CreateView,
                                                            UpdateView, DeleteView)

from .models import Cart, CartItem
from product.models import Product
from users.models import Profile
from cart.models import WishListItem,Order

#----------------Order views---------------------------------

@login_required
def order_view(request):
    context={
    }
    return render(request,'order/order.html',context)

@login_required
def order_list_view(request):
    ORDER_STATUS=((0,'Processing'),
                  (1,'Packed by the seller'),
                  (2,'Picked up from seller'),
                  (3,'Out for delivery'),
                  (4,'Reviewed'),
                  (5,'Delivered'),
                  (6,'On Hold')
                 )
    list_orders = Order.objects.filter(cart = Cart.objects.get(user = request.user.profile))
    final_orders={}
    for order in list_orders:
        final_orders[order] = ORDER_STATUS[order.status][1]
    context={
        'orders':final_orders
    }
    return render(request,'order/list_orders.html',context)

@login_required
def order_checkout_view(request):
    context={
        'options':("Credit Card","Net Banking","Cash On Delivery")
    }
    return render(request,'order/checkout.html',context)

@login_required
def order_success_view(request):
    c = Cart.objects.get(user = request.user.profile)
    cartitems = CartItem.objects.filter(cart = c)
    print(cartitems)
    total = 0
    for cart in cartitems :
        total+=cart.citem_price()
    order = Order.objects.create(cart = c,total = total)
    context={

    }
    return render(request,'order/success.html',context)
