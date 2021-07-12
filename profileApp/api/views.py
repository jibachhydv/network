from rest_framework import generics
from .serializers import ProfileSerializer
from profileApp.models import Profile
from rest_framework import permissions

from rest_framework.parsers import MultiPartParser, FormParser


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]


class SingleProfile(generics.RetrieveUpdateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]
