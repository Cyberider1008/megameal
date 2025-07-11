from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views.user import RegisterViewSet
from accounts.views.points import LoyaltyPointsView

router = DefaultRouter()
router.register('register', RegisterViewSet, basename='register')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('loyalty/', LoyaltyPointsView.as_view()),
] + router.urls
