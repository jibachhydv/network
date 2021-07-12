from .views import PostList
from django.urls import path

urlpatterns = [
    path("", PostList.as_view()),
]
