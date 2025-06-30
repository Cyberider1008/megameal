from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from products.services.product_service import is_product_in_stock, get_similar_products_based_on_history

class ProductStockCheckView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product_id")
        if not product_id:
            return Response({"error": "product_id required"}, status=400)
        in_stock = is_product_in_stock(product_id)
        return Response({"in_stock": in_stock})

class SmartMealSuggestionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        suggested_products = get_similar_products_based_on_history(request.user)
        data = [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "is_veg": p.is_veg
            }
            for p in suggested_products
        ]
        return Response({"suggested_meal": data})
