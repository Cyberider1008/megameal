# products/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views.product import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = router.urls