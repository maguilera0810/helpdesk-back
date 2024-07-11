# .\api\authentication\serializers\auth_serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

from apps.authentication.models import Profile
from apps.authentication.serializers import ProfileSerializer


class ProfilePublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "document",
            "document_type",
            "phone",
            "address",
            "is_available")


class UserPublicSerializer(serializers.ModelSerializer):
    profile = ProfilePublicSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile",
        )


class UserAdminSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        exclude = (
            "password",
        )


class UserAdminListSerializer(serializers.ModelSerializer):
    profile = ProfilePublicSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile",
        )


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    document = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        document = attrs.get("document")
        password = attrs.get("password")
        if not email and not document:
            raise serializers.ValidationError("Invalid credentials")
        user = None
        if email:
            user = User.objects.filter(email=email).first()
        elif document:
            user = User.objects.filter(profile__document=document).first()
        if user is None or not user.check_password(password):
            raise serializers.ValidationError("Invalid credentials.")
        attrs["user"] = user
        return attrs
