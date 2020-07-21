from django.shortcuts import render,redirect
from django.db.models import Q
from market.models import Market
from product.models import Product
from pages.models import Category,SubCategory,Slide
from django.views.generic import CreateView
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                       UserPassesTestMixin)
from django.core.paginator import Paginator
# Create your views here.

class SlidesCreateView(CreateView):
    model = Slide
    fields=['image']

def home_view(request):
    search=False
    context={
        "search":False,
    }
    #Homepage STARTS

    #SlideShow part
    first_slide,rest_slides = Slide.objects.all().first(),Slide.objects.all()[1:]
    context['first_slide'] = first_slide
    context['rest_slides'] = rest_slides

    #Category Part
    p_categories= Category.objects.filter(is_service = False)
    products={}
    for cate in p_categories :
        products[cate] = Product.objects.filter(Q(category=cate)&Q(approved=True))[:15]
    context["products"] = products

    s_categories= Category.objects.filter(is_service = True)
    services={}
    for cate in s_categories :
        services[cate] = Product.objects.filter(Q(category=cate)&Q(approved=True))[:15]
    context["services"] = services

    # context["categories"] = categories


    #Search Part STARTS
    if "search" in request.GET:
        query=request.GET['search'].lower()
        result=Product.objects.filter(  Q(tags__name__in=[query]) |Q(title__icontains=query) |Q(description__icontains=query)).distinct()

        # paginator = Paginator(result,2) # Show 25 contacts per page.
        # page_request_var = "page"
    	# page = request.GET.get(page_request_var)
    	# try:
    	#     page_obj = paginator.page(page)
    	# except PageNotAnInteger:
    	# 	# If page is not an integer, deliver first page.
    	# 	page_obj = paginator.page(1)
    	# except EmptyPage:
    	# 	# If page is out of range (e.g. 9999), deliver last page of results.
    	# 	page_obj = paginator.page(paginator.num_pages)

        paginator = Paginator(result,2) # Show 2 products per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        search=True
        context["search"]=True
        context["page_obj"]=page_obj
    #Seacrh part ENDS

    return render(request,"pages/home.html",context)

def search_view(request):
    context={}
    if "search" in request.GET:
        query=request.GET['search'].lower()
        result=Product.objects.filter(                    Q(tags__name__in=[query]) |Q(title__icontains=query) |Q(description__icontains=query)).distinct()

        # paginator = Paginator(result,2) # Show 25 contacts per page.
        # page_request_var = "page"
    	# page = request.GET.get(page_request_var)
    	# try:
    	#     page_obj = paginator.page(page)
    	# except PageNotAnInteger:
    	# 	# If page is not an integer, deliver first page.
    	# 	page_obj = paginator.page(1)
    	# except EmptyPage:
    	# 	# If page is out of range (e.g. 9999), deliver last page of results.
    	# 	page_obj = paginator.page(paginator.num_pages)

        paginator = Paginator(result,2) # Show 2 products per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        search=True
        context["search"]=True
        context["page_obj"]=page_obj
    return render(request,"pages/search.html",context)

def category_view(request,short):
    context = {
        "name":Category.objects.filter(short = short).first(),

    }
    subcategories = SubCategory.objects.filter(category__short = short)
    products = {}
    for sc in subcategories :
        products[sc] = Product.objects.filter(subcategory__short = sc.short)
    # print(products)
    context["products"] = products
    return render(request,"pages/category.html",context)
