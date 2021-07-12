from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializers
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.AllowAny, ]
    pagination_class = StandardResultsSetPagination