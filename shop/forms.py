from django import forms
from .models import Shop
class Shop_Form(forms.ModelForm):
    class Meta:
        model = Shop
        fields=[
            "title",
            "description",
            "category",
            "shopno",
            "address_line1",
            "address_line2",
            "contact_person",
            "contactno",
            "image",
            "market",
        ]
