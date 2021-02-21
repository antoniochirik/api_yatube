#from django.contrib.auth.models import User
from rest_framework import serializers

from posts.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    #post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = '__all__'
