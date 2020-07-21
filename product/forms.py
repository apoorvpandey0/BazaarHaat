from django import forms
from .models import Product,Review
from shop.models import Shop
# class Product_Form(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields =['title','image','actual_price','my_price','category',
#                                             'stock','shop','description','summary']

    # def __init__(self, *args, **kwargs):
        # self.fields['shop'].queryset = Shop.objects.filter(shopno=24)
    #     pass

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text','rating']
