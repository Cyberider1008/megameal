from rest_framework import generics, permissions
from carts.models import Cart
from carts.serializers import CartSerializer

class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Cart.objects.get_or_create(user=self.request.user)[0]
