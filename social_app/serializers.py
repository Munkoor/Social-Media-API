from rest_framework import serializers

from social_app.models import (
    UserProfile,
)


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("id", "user", "bio", "profile_picture")
