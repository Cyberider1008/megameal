from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models.category import Category
from products.models.product import Product

@receiver(post_save, sender=Category)
def handle_category_toggle(sender, instance, **kwargs):
    if not instance.is_active:
        Product.objects.filter(category=instance).update(is_active=False)
