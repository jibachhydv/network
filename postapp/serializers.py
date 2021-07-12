from rest_framework import serializers
from .models import Post, Comment, LikeModel


class PostSerializers(serializers.ModelSerializer):
    
    # post_author = 

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
        

class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LikeModel
        fields = "__all__"