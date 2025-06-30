from rest_framework import viewsets
from orders.models.order import Order
from orders.serializers.order import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
