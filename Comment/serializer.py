from rest_framework import serializers
from Post.serializer import PostSerializer,AuthorSerializer
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    owner = AuthorSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('post', 'comment','owner')
