from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class LoyaltyPointsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"loyalty_points": request.user.loyalty_points})
