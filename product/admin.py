from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportMixin
from import_export import resources

from .models import Review
from .models import Product

class ProductAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display    = ("title","description","shop","approved")
    search_fields   = ("title","tags")
    list_editable   = ('approved',)
    readonly_fields = ()
    filter_horizntal= ()
    list_filter     = ()
    fieldsets       = ()

class ProductResource(resources.ModelResource):
    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = Product
        fields = ('title', 'description','shop','approved',)
admin.site.register(Product,ProductAdmin)

admin.site.register(Review)
