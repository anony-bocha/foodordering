from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from .forms import CheckoutForm
from .models import Order, OrderItem
from products.models import Product
def checkout(request):
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(session_key=session_key)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                session_key=session_key,
                customer_name=form.cleaned_data['customer_name'],
                customer_email=form.cleaned_data['customer_email'],
                customer_address=form.cleaned_data['customer_address'],
            )
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.product_price
                )
            cart_items.delete()
            return redirect('order_success')
    else:
        form = CheckoutForm()

    return render(request, 'cart/checkout.html', {'form': form, 'cart_items': cart_items})

def order_success(request):
    return render(request, 'cart/order_success.html')

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
def checkout(request):
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(session_key=session_key)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                session_key=session_key,
                customer_name=form.cleaned_data['customer_name'],
                customer_email=form.cleaned_data['customer_email'],
                customer_address=form.cleaned_data['customer_address'],
            )
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.product_price
                )
            cart_items.delete()
            return redirect('order_success')
    else:
        form = CheckoutForm()

    return render(request, 'cart/checkout.html', {'form': form, 'cart_items': cart_items})
def order_success(request):
    return render(request, 'cart/order_success.html')
