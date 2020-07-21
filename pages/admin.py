from django.contrib import admin
from .models import Category,SubCategory,Tag,Slide
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(Slide)
# admin.site.register(Category2)
admin.site.site_header = "MAUJ Administration"
