from django.urls import path
from . import views

urlpatterns = [
    path('cart/update/<uuid:product_id>/', views.cart_update, name='cart_update'),
    path('add/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.order_success, name='order_success'),
]
