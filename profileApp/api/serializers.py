
from rest_framework import serializers
from profileApp.models import Profile

from rest_framework import serializers



class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    profile_picture = serializers.ImageField(use_url=True)

    class Meta:
        model = Profile
        fields = '__all__'
