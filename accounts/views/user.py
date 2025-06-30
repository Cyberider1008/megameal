from rest_framework import viewsets, permissions
from accounts.models.user import CustomUser
from accounts.serializers.user import RegisterSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
