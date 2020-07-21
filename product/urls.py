from django.urls import path
from . import views
urlpatterns=[
    path("product/<uuid:product_id>/",views.product_display_view,name="product-display-view"),
    path("product/create/",views.ProductCreateView.as_view(),name="product-create"),
    # path("product/create/",views.product_create_view,name="product-create"),
]

urlpatterns +=[
    path("review/delete/<uuid:r_id>/",views.review_delete_view,name="review-delete"),
]
