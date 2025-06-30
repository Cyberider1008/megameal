from rest_framework import viewsets
from products.models.category import Category
from products.serializers.category import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer