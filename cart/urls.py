from django.urls import path, include
from . import order_views
from . import cart_views
from . import wishlist_views

urlpatterns=[]

# CartItem Urls
urlpatterns += [
    path('cartitem/', cart_views.list_cartitem_view, name='list-cartitem'),
    #not_used path('cartitem/<int:pk>/', views.DetailCartItem.as_view(), name='detail-cartitem'),
    #alt path('cartitem/create/', views.CreateCartItem.as_view(), name='create-cartitem'),
    path('cartitem/create/<uuid:p_id>/', cart_views.create_cartitem_view, name='create-cartitem'),
    #not_used path('cartitem/<int:pk>/update/', views.UpdateCartItem.as_view(), name='update-cartitem'),
    #alt path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(), name='delete-cartitem'),
    path('cartitem/delete/<uuid:p_id>/', cart_views.delete_cartitem_view, name='delete-cartitem'),
]

urlpatterns+=[
    path('order/',order_views.order_view,name='order'),
    path('orders/',order_views.order_list_view,name='order-list'),
    path('order/checkout/',order_views.order_checkout_view,name='order-checkout'),
    path('order/success/',order_views.order_success_view,name='order-success'),
]

urlpatterns += [
    # path('wishlistitem/', wishlist_views.WLItem, name='list-wishlistitem'),
    path('wishlistitem/create/<uuid:p_id>/', wishlist_views.create_wishlistitem_view, name='create-wishlistitem'),
    path('wishlistitem/delete/<uuid:p_id>/', wishlist_views.delete_wishlistitem_view, name='delete-wishlistitem'),
    path('wishlistitem/move/<uuid:p_id>/', wishlist_views.move_wishlistitem_view, name='move-wishlistitem'),
]

# Cart Urls
urlpatterns += [
    # path('cart/', views.ListCart, name='list-carts'),
    # path('cart/<int:pk>/', views.DetailCart.as_view(), name='detail-cart'),
    # path('cart/create/', views.CreateCart.as_view(), name='create-cart'),
    # path('cart/<int:pk>/update/', views.Updatecart.as_view(), name='update-cart'),
    # path('cart/<int:pk>/delete/', views.DeleteCart.as_view(), name='delete-cart'),
]
