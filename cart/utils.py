from .models import CartItem


def merge_carts(session_key, user):
    if not session_key or not user.is_authenticated:
        return

    session_cart_items = CartItem.objects.filter(session_key=session_key)
    user_cart_items = CartItem.objects.filter(user=user)

    for item in session_cart_items:
        # Check if product exists in user cart
        existing_item = user_cart_items.filter(product=item.product).first()
        if existing_item:
            existing_item.quantity += item.quantity
            existing_item.save()
        else:
            item.user = user
            item.session_key = ""
            item.save()

    # Delete all session cart items that are now merged or transferred
    session_cart_items.filter(user__isnull=True).delete()
