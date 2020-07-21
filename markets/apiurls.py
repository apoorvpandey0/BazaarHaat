from django.urls import path,include
#The imports below are necessary for MEDIA to work

urlpatterns = [
    path('product/', include('product.api.urls'),name = 'api-product'),
    path('pages/', include('pages.api.urls'),name = 'api-pages'),
    path('cart/', include('cart.api.urls'),name = 'api-cart'),
]
