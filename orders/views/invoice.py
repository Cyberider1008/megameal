from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import FileResponse
from orders.models.order import Order
from orders.utils.invoice import generate_invoice

class InvoiceDownloadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, customer=request.user)
            buffer = generate_invoice(order)
            return FileResponse(buffer, as_attachment=True, filename=f"invoice_{order_id}.pdf")
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)
