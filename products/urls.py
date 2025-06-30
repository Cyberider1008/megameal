from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views.category import CategoryViewSet
from products.views.product import ProductViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = router.urls