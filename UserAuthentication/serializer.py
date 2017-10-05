from django.contrib.auth.models import User
from rest_framework import serializers
from UserProfile.serializer import UserProfileSerializer
from Post.serializer import PostSerializer
from Connection.models import Follower


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    user_profile = UserProfileSerializer(read_only=True)
    posts = PostSerializer(read_only=True, many=True)
    following_count = serializers.SerializerMethodField()
    follower_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password', 'follower_count', 'following_count',
            'user_profile', 'posts')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_following_count(self, obj):
        return obj.followings.all().count()

    def get_follower_count(self, obj):
        return obj.followers.all().count()
