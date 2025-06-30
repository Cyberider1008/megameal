from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from products.models.product import Product
from django.db.models import Q

class ProductSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.GET.get("q", "")
        category = request.GET.get("category")
        is_veg = request.GET.get("is_veg")

        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

        if category:
            products = products.filter(category__name__iexact=category)
        if is_veg in ["true", "false"]:
            products = products.filter(is_veg=(is_veg == "true"))

        data = [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "category": p.category.name,
                "stock": p.stock,
                "is_veg": p.is_veg
            } for p in products if p.stock > 0 and p.is_active
        ]
        return Response({"results": data})
