from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (DetailView, ListView, CreateView,UpdateView, DeleteView)

from .models import Cart, CartItem
from product.models import Product
from users.models import Profile
from cart.models import WishListItem

#....-------------- Cart Views --------------------------------------
class ListCartItem(ListView):
    model = CartItem
    context_object_name = 'cartitems'
    template_name='cartitem/list_cartitems.html'

def list_cartitem_view(request):
    c=Cart.objects.get(user=request.user.profile)
    cartitems = CartItem.objects.filter(cart = c)
    wishlistitems = WishListItem.objects.all()
    context = {
        'wishlistitems': wishlistitems,
        'cartitems': cartitems,
    }
    return render(request,'cartitem/list_cartitems.html',context)

@login_required
def create_cartitem_view(request,p_id):
    p=Product.objects.get(id=p_id)
    c=Cart.objects.get(user=request.user.profile)
    new=CartItem.objects.create(cart=c,product=p)
    new.save()
    messages.success(request,"Product successfully added to Cart")
    return redirect('list-cartitem')

@login_required
def delete_cartitem_view(request,p_id):
    instance=CartItem.objects.get(id=p_id)
    instance.delete()
    messages.success(request,"Product successfully removed from Cart")
    return redirect('list-cartitem')
