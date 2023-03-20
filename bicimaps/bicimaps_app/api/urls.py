from django.urls import path, include
from ..views.user_creation_view import UserCreationView

urlpatterns = [
    path('sign-up/', UserCreationView.as_view()),
]