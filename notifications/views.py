from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notifications.services.alert_service import create_stock_alert

class CreateProductAlertView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product_id")
        if not product_id:
            return Response({"error": "product_id required"}, status=400)
        create_stock_alert(request.user, product_id)
        return Response({"message": "Alert created. You'll be notified when product is back in stock."})
