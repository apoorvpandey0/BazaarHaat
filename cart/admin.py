from django.contrib import admin
from .models import Cart,CartItem,Order,WishListItem,Coupon
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display    = ("cart",'datetime','status','total')
    search_fields   = ("status",'cart')
    # list_editable   = ('status'),
    readonly_fields = ('cart','datetime','total')
    filter_horizntal= ()
    list_filter     = ("status"),
    fieldsets       = ()
admin.site.register(Order,OrderAdmin)

admin.site.register(Coupon)

admin.site.register(Cart)
admin.site.register(CartItem)

admin.site.register(WishListItem)
