from django.urls import path
from reviews.views import ReviewCreateListView

urlpatterns = [
    path('<int:product_id>/reviews/', ReviewCreateListView.as_view()),
]