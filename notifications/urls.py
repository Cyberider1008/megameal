from django.urls import path
from notifications.views import CreateProductAlertView
from notifications.views import NotificationListView, NotificationMarkAsReadView


urlpatterns = [
    path('create-alert/', CreateProductAlertView.as_view()),
    path('', NotificationListView.as_view()),
    path('<int:pk>/read/', NotificationMarkAsReadView.as_view()),

]