from re import A
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from orders.models.order import Order
from orders.services.razorpay_service import create_razorpay_order, verify_signature
from rest_framework.permissions import AllowAny

class CreateRazorpayOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [AllowAny]

    def post(self, request):
        amount = request.data.get('amount')
        local_order_id = request.data.get('order_id')
        if not local_order_id or not amount:
            return Response({"error": "order_id and amount are required"}, status=400)
        try:
            order = Order.objects.get(id=local_order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        payment = create_razorpay_order(float(amount))
        
        order.razorpay_order_id = payment['id']
        order.save()
        return Response(payment)



class VerifyRazorpayPaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [AllowAny]

    def post(self, request):
        
        order_id = request.data.get("razorpay_order_id")
        payment_id = request.data.get("razorpay_payment_id")
        signature = request.data.get("razorpay_signature")
        order_db = Order.objects.filter(razorpay_order_id=order_id).first()
          
        

        if order_db and verify_signature(order_id, payment_id, signature):
            order_db.payment_status = "paid"
            order_db.razorpay_payment_id = payment_id
            order_db.razorpay_signature = signature
            order_db.save()
            return Response({"message": "Payment verified and updated"})
        return Response({"error": "Payment verification failed"}, status=400)

