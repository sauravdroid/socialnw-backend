from rest_framework import serializers
from UserAuthentication.serializer import UserSerializer
from Post.serializer import PostSerializer
from .models import *


class RequestSerializer(serializers.ModelSerializer):
    request_status = serializers.BooleanField(read_only=True)
    user = UserSerializer(read_only=True)
    requested_user = UserSerializer(read_only=True)
    request_date = serializers.DateField(read_only=True)

    class Meta:
        model = Request
        fields = ('request_status', 'user', 'requested_user', 'request_date')


class FollowerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    follower = UserSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = ('user', 'follower')


class AllFollowerSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = ('follower',)

class AllFollowingSerializer(serializers.ModelSerializer):
    following_user = UserSerializer(read_only=True)

    class Meta:
        model = Following
        fields = ('following_user',)


class FollowerPostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = ('posts',)
