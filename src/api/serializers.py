from rest_framework import serializers
from posts.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment',]