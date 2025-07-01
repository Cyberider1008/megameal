from rest_framework import serializers
from carts.models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source='cartitem_set', many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'updated_at', 'checked_out', 'items']
        read_only_fields = ['user']