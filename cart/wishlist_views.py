from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (DetailView, ListView, CreateView,UpdateView, DeleteView)

from .models import Cart, CartItem
from product.models import Product
from users.models import Profile
from cart.models import WishListItem
#--------------------WishListItem views------------------------------
@login_required
def create_wishlistitem_view(request,p_id):
    p=Product.objects.filter(id=p_id).first()
    c=Cart.objects.filter(user=request.user.profile).first()
    new=WishListItem.objects.create(cart=c,product=p)
    new.save()
    messages.success(request,"Product Successfully added to wishlist")
    return redirect('list-cartitem')

@login_required
def delete_wishlistitem_view(request,p_id):
    instance=WishListItem.objects.get(id=p_id)
    instance.delete()
    messages.success(request,"Product successfully removed from wishlist.")
    return redirect('list-cartitem')

@login_required
def move_wishlistitem_view(request,p_id):
    wlitem = WishListItem.objects.get(id = p_id)
    p=wlitem.product
    c=Cart.objects.get(user=request.user.profile)
    cartitem=CartItem.objects.create(cart=c,product=p)
    cartitem.save()

    wlitem=WishListItem.objects.get(id=p_id)
    wlitem.delete()

    messages.success(request,"Product Successfully moved to cart")
    return redirect('list-cartitem')
