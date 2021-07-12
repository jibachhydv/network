from rest_framework import serializers
from postapp.models import Post, Comment, LikeModel


class PostSerializers(serializers.ModelSerializer):

    author_name = serializers.SerializerMethodField(
        'get_username_from_post_author')

    author = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Post
        fields = "__all__"

    def get_username_from_post_author(self, post):
        username = post.author.first_name + " " + post.author.last_name
        return username

    


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikeModel
        fields = "__all__"
