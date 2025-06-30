from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.views.order import OrderViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet)

urlpatterns = router.urls