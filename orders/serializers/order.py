from rest_framework import serializers
from orders.models.order import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_type', 'status', 'shipping_address', 'discount', 'total_price',
                  'payment_status', 'razorpay_order_id', 'razorpay_payment_id', 'razorpay_signature',
                  'items', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items_data:
            OrderItem.objects.create(order=order, **item)
        return order


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'order_type', 'shipping_address', 'discount', 'created_at']
        read_only_fields = ['id', 'order_type', 'shipping_address', 'discount', 'created_at']
