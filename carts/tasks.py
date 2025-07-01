from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from carts.models import Cart
from django.core.mail import send_mail

@shared_task
def send_abandoned_cart_emails():
    cutoff = timezone.now() - timedelta(hours=24)
    abandoned_carts = Cart.objects.filter(updated_at__lt=cutoff, checked_out=False)
    for cart in abandoned_carts:
        user = cart.user
        if user.email:
            send_mail(
                subject="🛒 You left items in your MegaMeal cart!",
                message="Looks like you forgot something! Complete your checkout today and enjoy your meal.",
                from_email="noreply@megameal.com",
                recipient_list=[user.email],
            )