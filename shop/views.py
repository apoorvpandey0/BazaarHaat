from django.shortcuts import render,redirect
from .forms import Shop_Form
from .models import Shop
from product.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.contrib.auth.models import User
from shop.models import Shop
from .decorators import is_shop_owner
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                       UserPassesTestMixin)
# Create your views here.
def seller_shop_view(request,shop_id):
    context={
    }
    return render(request,"shop/seller_shop_view.html",context)

class ShopCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Shop
    fields = ['title','GSTIN','category','market','contact_person','address_line1',
              'address_line2','pincode']

    #This sets the author of the post to the current logged in User
    def form_valid(self,form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.is_seller == False:
            return True
        else:
            return False
@is_shop_owner
def shop_view(request,shop_id):
    obj=Shop.objects.filter(id=shop_id)
    context={
        "shop":obj[0],
        "products":Product.objects.filter(shop=obj[0])
    }
    return render(request,"product/product_list.html",context)

def shop_approval_view(request):
    return render(request,'shop/approval.html',{})
