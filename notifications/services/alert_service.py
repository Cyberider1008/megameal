from notifications.models import ProductAlert
from products.models.product import Product

def create_stock_alert(user, product_id):
    alert, created = ProductAlert.objects.get_or_create(user=user, product_id=product_id, notified=False)
    return alert

def check_and_notify_back_in_stock():
    alerts = ProductAlert.objects.filter(notified=False)
    for alert in alerts:
        product = alert.product
        if product.stock > 0:
            # Placeholder for real notification logic (email/sms)
            print(f"Notify {alert.user.email}: {product.name} is now in stock!")
            alert.notified = True
            alert.save()
