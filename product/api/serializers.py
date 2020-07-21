from rest_framework import serializers

from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from django.urls import reverse

from ..models import Product,Review
from shop.models import Shop

class ProductCreateSerializer(TaggitSerializer,serializers.ModelSerializer):
    tags  = TagListSerializerField()

    def perform_create(self, serializer):
        #To associate current user wih the new model bieng created
        serializer.save(seller = self.request.user.profile,
                        shop= Shop.objects.get(owner=self.request.user.profile.id))

    class Meta:
        model = Product
        fields =['id','title','image','tags','actual_price','my_price','category','subcategory','stock','description','summary']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id','title','image','actual_price','my_price','category','subcategory','stock','description','summary']


class ProductListSerializer(serializers.ModelSerializer):
    #Add Custom URL's to the JSON data of each Product
    product_detail_url = serializers.HyperlinkedIdentityField(
    view_name = 'api-product-detail',
    # lookup_field = 'id',
    )
    #Custom Field values
    seller = serializers.SerializerMethodField()
    #Adding Markdown
    html = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields =['html','product_detail_url','id','title','image','seller','actual_price','my_price','category','subcategory','stock','description','summary']

    def get_seller(self,obj):
        return str(obj.seller.user.username)

    def get_html(self,obj):
        return obj.get_markdown()

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id','title','image','actual_price','my_price','category','subcategory','stock','description','summary']


class ProductUpdateStockSerializer(serializers.ModelSerializer):
    def perform_update(self, serializer):
        #To associate current user wih the new model bieng created
        serializer.save(seller = self.request.user.profile,
                        shop= Shop.objects.get(owner=self.request.user.profile.id))
        #MAybe Send Email
    class Meta:
        model = Product
        fields =['stock']

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','product','user','text','rating','created']




data ={
        "id": "8875b4a0-0554-4d12-a515-e4cf3063f558",
        "title": "Mast cheez 4",
        "image": "http://localhost:8000/media/products/amoonguss.png",
        "actual_price": "100.00",
        "my_price": "80.00",
        "category": 1,
        "subcategory": 1,
        "stock": 0,
        "description": "This product is cool!",
        "summary": "I love this product"
    }
# >>> if new.is_valid():
# ...     new.save()
# ... else:
# ...     print(new.errors)
# ...
