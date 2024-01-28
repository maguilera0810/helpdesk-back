from django.contrib.auth.models import User
from rest_framework import serializers

from apps.authentication.models import Profile
from apps.common.serializers import SkillSerializer


class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # skills = SkillSerializer(many=True)

    class Meta:
        model = Profile
        fields = (
            'id',
            # 'user',
            'phone_number',
            'address',
            'is_available',
            'external_code',
            'skills')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
        )
