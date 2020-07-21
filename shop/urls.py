from django.urls import path
from .views import (shop_approval_view,
                   shop_view,
                   ShopCreateView,
                   seller_shop_view)
urlpatterns=[
    path("shop/register/",ShopCreateView.as_view(),name="shop-create"),
    path("shop/approval/",shop_approval_view,name="shop-approval"),
    path("shop/<uuid:shop_id>/",shop_view,name="shop-view"),
    # path("shop/profile/<int:shop_id>/",seller_shop_view,name="seller-shop-view"),
]
