# .\api\authentication\serializers\auth_serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

from apps.authentication.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
