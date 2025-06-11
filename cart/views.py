from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from products.models import Product

def add_to_cart(request, product_id):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    product = get_object_or_404(Product, uid=product_id)
    cart_item, created = CartItem.objects.get_or_create(session_key=session_key, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')

def view_cart(request):
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})
