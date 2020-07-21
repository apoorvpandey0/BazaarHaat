from django.urls import path

from . import views

urlpatterns=[
    path('list/',views.ProductListAPIView.as_view(),name = 'api-product-list'),
    path('create/',views.ProductCreateAPIView.as_view(),name = 'api-product-create'),
    path("detail/<uuid:pk>/",views.ProductDetailAPIView.as_view(),name="api-product-detail"),
    path("update/<uuid:pk>/",views.ProductUpdateAPIView.as_view(),name="api-product-update"),
    path("update/stock/<uuid:pk>/",views.ProductUpdateStockAPIView.as_view(),name="api-product-update-stock"),
    path("delete/<uuid:pk>/",views.ProductDeleteAPIView,name="api-product-delete"),
]

urlpatterns +=[
    path("review/list/",views.ReviewListAPIView.as_view(),name="api-review-list"),
]
