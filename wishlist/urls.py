from django.urls import path
from wishlist.views import WishlistListCreateView, WishlistDeleteView

urlpatterns = [
    path('', WishlistListCreateView.as_view()),
    path('<int:pk>/delete/', WishlistDeleteView.as_view()),
]