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
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
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
    product = get_object_or_404(Product, uid=product_id)

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart_item, created = CartItem.objects.get_or_create(session_key=session_key, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    if request.user.is_authenticated:
        count = CartItem.objects.filter(user=request.user).count()
    else:
        count = CartItem.objects.filter(session_key=session_key).count()

    request.session['cart_count'] = count

    return redirect('cart_detail')

def checkout(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
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
                user=request.user if request.user.is_authenticated else None,
                session_key=session_key if not request.user.is_authenticated else '',
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
        if request.user.is_authenticated:
            cart_item = CartItem.objects.filter(user=request.user, product_id=product_id).first()
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            cart_item = CartItem.objects.filter(session_key=session_key, product_id=product_id).first()

        if cart_item:
            action = request.POST.get('action')
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

        if request.user.is_authenticated:
            count = CartItem.objects.filter(user=request.user).count()
        else:
            count = CartItem.objects.filter(session_key=session_key).count()

        request.session['cart_count'] = count

    return redirect('cart_detail')


def order_success(request):
    return render(request, 'cart/order_success.html')
