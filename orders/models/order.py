from django.db import models
from accounts.models.user import CustomUser
from products.models.product import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('cancelled', 'Cancelled')
    ]
    TYPE_CHOICES = [
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
        ('dinein', 'Dine-in')
    ]

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    shipping_address = models.TextField(blank=True, null=True)
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    loyalty_points_awarded = models.IntegerField(default=0)


    payment_status = models.CharField(max_length=10, choices=[
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('failed', 'Failed')
    ], default='unpaid')
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"Order #{self.id} - {self.customer.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
