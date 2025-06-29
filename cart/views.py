
from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem, Order, OrderItem
from .forms import CheckoutForm
from products.models import Product
from django.contrib import messages


def cart_count(request):
    session_key = request.session.session_key
    if not session_key:
        return {'cart_count': 0}
    count = CartItem.objects.filter(session_key=session_key).count()
    return {'cart_count': count}

def view_cart(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart_items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.total_price for item in cart_items)

    request.session['cart_count'] = cart_items.count()

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

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

    request.session['cart_count'] = CartItem.objects.filter(session_key=session_key).count()

    return redirect('view_cart')

def checkout(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart_items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.total_price for item in cart_items)

    request.session['cart_count'] = cart_items.count()

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
            request.session['cart_count'] = 0
            messages.success(request, "Your order has been placed successfully!")
            return redirect('order_success')
    else:
        form = CheckoutForm()

    return render(request, 'cart/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'total': total
    })

def cart_update(request, product_id):
    if request.method == 'POST':
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        action = request.POST.get('action')
        cart_item = CartItem.objects.filter(session_key=session_key, product_id=product_id).first()

        if cart_item:
            if action == 'increment':
                cart_item.quantity += 1
                cart_item.save()
            elif action == 'decrement':
                if cart_item.quantity > 1:
                    cart_item.quantity -= 1
                    cart_item.save()
                else:
                    cart_item.delete()
            elif action == 'remove':
                cart_item.delete()

        request.session['cart_count'] = CartItem.objects.filter(session_key=session_key).count()

    return redirect('view_cart')

def order_success(request):
    return render(request, 'cart/order_success.html')