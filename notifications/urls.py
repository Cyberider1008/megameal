from django.urls import path
from notifications.views import CreateProductAlertView

urlpatterns = [
    path('create-alert/', CreateProductAlertView.as_view()),
]