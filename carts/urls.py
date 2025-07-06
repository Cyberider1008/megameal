from django.urls import path
from carts.views import CartDetailView


urlpatterns = [
    path('', CartDetailView.as_view()),
    
]