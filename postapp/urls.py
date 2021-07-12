from .api.views import PostList, PostDetail
from django.urls import path

urlpatterns = [
    path("", PostList.as_view(), name="post_lists"),
    path("<int:pk>", PostDetail.as_view(), name="post_detail"),
]
