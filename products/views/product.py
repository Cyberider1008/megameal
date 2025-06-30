from rest_framework import viewsets
from products.models.product import Product
from products.serializers.product import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer