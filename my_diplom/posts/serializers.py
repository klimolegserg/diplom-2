from rest_framework import serializers
from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'created_at', 'image', 'comments', 'total_likes']
        read_only_fields = ['user']
