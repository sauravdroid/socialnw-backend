from .models import Profile
from rest_framework import serializers
from .models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('intro', 'profile_pic')
