from rest_framework import serializers
from .models import Post, PostLike
from django.contrib.auth.models import User
from UserProfile.serializer import UserProfileSerializer
from Comment.models import Comment


class AuthorSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'user_profile')


class SerializerComments(serializers.ModelSerializer):
    owner = AuthorSerializer(read_only=True)
    comment = serializers.CharField(read_only=True)
    commented_at = serializers.DateField(read_only=True)

    class Meta:
        model = Comment
        fields = ('comment', 'owner', 'commented_at')


class PostLikeSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only=True)

    class Meta:
        model = PostLike
        fields = ('like_status', 'user')


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(read_only=True)
    pk = serializers.IntegerField(read_only=True)
    owner = AuthorSerializer(read_only=True)
    post_comments = SerializerComments(read_only=True, many=True)
    post_likes = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    current_user_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'title', 'subheader', 'content', 'cover_pic', 'created_at', 'pk', 'owner', 'current_user_liked',
            'like_count', 'post_comments',
            'post_likes')

    def get_post_likes(self, obj):

        likes = PostLike.objects.filter(like_status=True, post=obj)
        like_serializer = PostLikeSerializer(likes, many=True)
        return like_serializer.data

    def get_like_count(self, obj):
        likes = PostLike.objects.filter(like_status=True, post=obj)
        return likes.count()

    def get_current_user_liked(self, obj):
        try:
            likeInstance = PostLike.objects.get(post=obj, user=self.context['request'].user)
        except PostLike.DoesNotExist:
            return False
        return likeInstance.like_status

