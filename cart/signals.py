from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.sessions.models import Session
from .utils import merge_carts

@receiver(user_logged_in)
def handle_cart_merge(sender, request, user, **kwargs):
    session_key = request.session.session_key
    merge_carts(session_key, user)
