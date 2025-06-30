from rest_framework import generics, permissions
from orders.models.order import Order
from orders.serializers.order import OrderStatusSerializer

class OrderStatusUpdateView(generics.UpdateAPIView):
    serializer_class = OrderStatusSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAdminUser]

class OrderStatusView(generics.RetrieveAPIView):
    serializer_class = OrderStatusSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
