from rest_framework import serializers

from profiles_api.models import UserProfile


class HelloApiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'is_active']

