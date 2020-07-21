from django.urls import path
from . import views

urlpatterns = [
    path('order/update/<uuid:pk>/',views.OrderUpdateAPIView.as_view(),name = 'api-cart-order-update-status'),
]
