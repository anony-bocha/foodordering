from django.urls import path
from . import views  # Adjust import depending on your cart app structure

urlpatterns = [
    # Other app urls
    path('cart/', views.view_cart, name='cart_detail'),  # matches the URL used in base.html
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
]
