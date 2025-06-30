from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from coupons.models import Coupon
from orders.models.order import Order
from orders.services.discount import apply_coupon

class ApplyCouponView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, customer=request.user)
            coupon_code = request.data.get("coupon")
            coupon = Coupon.objects.get(code=coupon_code)
            discount = apply_coupon(order, coupon)
            if discount > 0:
                order.coupon = coupon
                order.discount_applied = discount
                order.save()
                return Response({"success": True, "discount": discount})
            return Response({"success": False, "message": "Coupon not applicable."}, status=400)
        except (Order.DoesNotExist, Coupon.DoesNotExist):
            return Response({"error": "Invalid order or coupon."}, status=400)
