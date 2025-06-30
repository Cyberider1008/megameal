from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.views.order import OrderViewSet
from orders.views.payment import CreateRazorpayOrderView, VerifyRazorpayPaymentView
from orders.views.stock_check import ProductStockCheckView, SmartMealSuggestionView
from orders.views.tracking import OrderStatusUpdateView, OrderStatusView
from orders.views.invoice import InvoiceDownloadView
from orders.views.apply_coupon import ApplyCouponView



router = DefaultRouter()
router.register('orders', OrderViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('create-razorpay-order/', CreateRazorpayOrderView.as_view()),
    path('verify-razorpay-payment/', VerifyRazorpayPaymentView.as_view()),

    path('check-stock/', ProductStockCheckView.as_view()),
    path('smart-meal/', SmartMealSuggestionView.as_view()),

    path('status/<int:pk>/', OrderStatusView.as_view()),
    path('status/<int:pk>/update/', OrderStatusUpdateView.as_view()),

    path('invoice/<int:order_id>/download/', InvoiceDownloadView.as_view()),
    
    path('order/<int:order_id>/apply-coupon/', ApplyCouponView.as_view()),

]
