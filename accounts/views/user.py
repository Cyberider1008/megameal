# accounts/views/user.py
from rest_framework import viewsets, permissions
from accounts.serializers.user import RegisterSerializer
from accounts.models.user import CustomUser

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
