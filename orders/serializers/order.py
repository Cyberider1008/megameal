# orders/serializers/order.py
from rest_framework import serializers
from orders.models.order import Order, OrderItem
from products.serializers.product import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_type', 'status', 'shipping_address', 'discount', 'total_price', 'items', 'created_at']
