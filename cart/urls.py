from django.urls import path
from . import views

urlpatterns = [
    path("cart/", views.view_cart, name="cart_detail"),
    path("cart/add/<uuid:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/update/<uuid:product_id>/", views.cart_update, name="cart_update"),
    path("checkout/", views.checkout, name="checkout"),
    path("order-success/", views.order_success, name="order_success"),
]
