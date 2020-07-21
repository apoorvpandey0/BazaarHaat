from django.shortcuts import render
from .models import Market
from shop.models import Shop
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from product.models import Product
from shop.models import Shop
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                       UserPassesTestMixin)
# Create your views here.
CATEGORY_CHOICES={
    'MED'  : 'Medical',
    'ELEC' : 'Electronics',
    'FOOD' : 'Food',
    'GEN'  : 'General',
    'CLTH' : 'Clothing',
    'STNY' : 'Stationary',
    'FOOT' : 'Footwear',
    'COSM' : 'Cosmetics',
    'TOYS' : 'Toys',
}
class MarketListView(ListView):
    model = Market
    context_object_name="markets"

class MarketCreateView(CreateView):
    model = Market
    fields= ['title','description','city','image']

def market_view(request,market_id):
    """This is the market category selector view,
            home->markets->market categories!
    """
    obj=Market.objects.filter(id=market_id)
    context={
        "market":obj[0],
        "shops" :Shop.objects.filter(market=obj[0],status=True),
        'cate'  :CATEGORY_CHOICES,
        "cate_val":CATEGORY_CHOICES.values(),
        "cate_key":CATEGORY_CHOICES.keys(),
    }
    return render(request,"pages/category.html",context)
def cate_shop_list_view(request,category_str,market_id):
    """This is the view of the shops in a market with certain category"""
    obj=Shop.objects.filter(category=category_str)
    obj2=[]
    #obj2 contains list of Shops sorted by market_id
    for item in obj :
        if item.market.id==market_id :
            obj2.append(item)
    context={
        "queryset":obj2,
        "total":True if len(obj2) else False
    }
    return render(request,"market/category.html",context)
def cate_shop_products_list_view(request,category_str,market_id,shop_id):
    prods=Product.objects.filter(category=category_str,shop__id=shop_id)
    context={
        "products":prods,
        "total":len(prods),
    }
    return render(request,"product/cate_shop_products_list_view.html",context)
