from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Product,Review
from shop.models import Shop
from .forms import ReviewForm
# from .forms import Product_Form
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                       UserPassesTestMixin)
class ProductCreateView(CreateView):
    model = Product
    fields =['title','image','actual_price','my_price','category','subcategory','stock','description','summary']
    #This sets the author of the post to the current logged in User
    def form_valid(self,form):
        form.instance.seller = self.request.user.profile
        form.instance.shop   = Shop.objects.filter(owner=self.request.user.profile.id).first()
        return super().form_valid(form)


def product_display_view(request,product_id):
    #Product Display
    obj=Product.objects.get(id=product_id)
    context={
        "item":obj
    }

    #Reviews
    # flag  = Review.objects.filter(user = request.user.profile,product = obj)


    # first_review = flag.first()
    # reviews = Review.objects.filter(product = obj)[:5]
    # context['first_review'] = first_review
    # context['reviews'] = reviews

    # if request.user.is_authenticated:
    #     reviewform = ReviewForm()
    #     context['reviewform'] = reviewform
    #     if request.method == 'POST' and len(flag)==0:
    #         form=ReviewForm(request.POST)
    #         if form.is_valid() :
    #             #The next step is necessary or else the form will not work
    #             new_form = form.save(commit=False)
    #             #Now set the form values
    #             new_form.user = request.user.profile
    #             new_form.product = obj
    #             #And save it
    #             new_form.save()
    #             messages.success(request,f"You have successfully reviewed this product.")
    #             return redirect('/product/{}/'.format(obj.id))
    #
    #     elif request.method =='POST' and len(flag)!=0:
    #         messages.success(request,f"You have already reviewed this product.")
    #         form=ReviewForm()
    #
    #     else :
    #         form = ReviewForm()

    #Similar Products
    tags = obj.tags.all()
    similar = []
    for tag in tags:
        similar += Product.objects.filter(tags = tag )
    similar = set(similar)
    similar = list(similar)
    if obj in similar :
        similar.remove(obj)
    context["similar"]=similar[:15]

    return render(request,"product/product_display.html",context)


def review_delete_view(request,r_id):
    obj = Review.objects.get(id = r_id).product
    Review.objects.get(id = r_id).delete()
    messages.success(request,"Review deleted.")
    return redirect('/product/'+str(obj.id)+'/')
