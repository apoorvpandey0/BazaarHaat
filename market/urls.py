from django.urls import path
from . import views

urlpatterns=[
    path("markets/",views.MarketListView.as_view(),name="market-list"),
    path("market/<int:market_id>/",views.market_view,name="market-view"),
    path("market/<int:market_id>/category/<str:category_str>/",
                views.cate_shop_list_view,
                name="category-view"),
    path("market/<int:market_id>/category/<str:category_str>/<int:shop_id>",
                views.cate_shop_products_list_view,
                name="cate-shop-view"),
    path("markets/create/",views.MarketCreateView.as_view(),name="market-create"),
]
