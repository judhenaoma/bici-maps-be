from django.urls import path, include
from ..views.user_creation_view import UserCreationView
from ..views.user_detail_view import UserDetailView
from ..views.review_creation_view import ReviewCreationView
from ..views.reviews_list_view import ReviewsListView

urlpatterns = [
    path('sign-up/', UserCreationView.as_view()),
    path('user-detail/', UserDetailView.as_view()),
    path('create-review/', ReviewCreationView.as_view()),
    path('reviews/', ReviewsListView.as_view()),
]