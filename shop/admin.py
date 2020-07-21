from django.contrib import admin
from .models import Shop
from django.contrib.admin import ModelAdmin

from import_export.admin import ImportExportMixin


class ShopAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display    = ("title","description","shopno","owner","market","status")
    search_fields   = ("title",'GSTIN')
    # list_editable   = ('status',)
    readonly_fields = ()
    filter_horizntal= ()
    list_filter     = ('category','status')
    fieldsets       = ()
admin.site.register(Shop,ShopAdmin)
