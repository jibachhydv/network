
from rest_framework import serializers
from profileApp.models import Profile

from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.SerializerMethodField('get_username')
    profile_picture = serializers.ImageField(use_url=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def get_username(self, profile):
        username = profile.user.first_name.capitalize(
        ) + " " + profile.user.last_name.capitalize()
        return username
