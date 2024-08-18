# .\api\authentication\serializers\auth_serializers.py
from copy import deepcopy

from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from apps.authentication.models import Profile
from apps.authentication.serializers import ProfileSerializer
from resources.enums import ValidatorMsgEnum
from resources.validators.field_validator import FieldValidator


class UserPublicSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False, read_only=True)

    class Meta:
        model = User
        exclude = ("password",)


class ProfileCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def validate_document(self, value):
        """
        Validate that the document is unique.
        """
        query = Profile.objects.filter(document=value)
        if self.instance:
            if query.exclude(id=self.instance.id).exists():
                raise ValidationError(ValidatorMsgEnum.DOCUMENT_ALREADY_EXIST)
        elif query.exists():
            raise ValidationError(ValidatorMsgEnum.USER_ALREADY_EXIST)
        return value


class UserCrudSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_email(self, value):
        is_ok, msg = FieldValidator.validate_email(value)
        if not is_ok:
            raise ValidationError(msg)
        query = User.objects.filter(email=value)
        if self.instance:
            if query.exclude(id=self.instance.id).exists():
                raise ValidationError(ValidatorMsgEnum.EMAIL_ALREADY_EXIST)
        elif query.exists():
            raise ValidationError(ValidatorMsgEnum.USER_ALREADY_EXIST)
        return value

    def validate_password(self, value):
        if self.instance is None and not value:
            raise ValidationError(ValidatorMsgEnum.PASSWORD_REQUIRED)
        if value:
            is_ok, msg = FieldValidator.validate_password(value)
            if not is_ok:
                raise ValidationError(msg)
        return value

    def validate(self, data: dict):
        request = self.context.get("request")
        if not request:
            return data
        request_user = request.user
        if not request_user:
            raise ValidationError(
                {"user": "no_request_user"})
        is_superuser = request_user.is_superuser
        if not is_superuser and self.instance and request_user.id != self.instance.id:
            raise ValidationError(ValidatorMsgEnum.DONT_HAVE_PERMISSION)
        restricted_fields = ("is_staff", "is_active", "is_superuser")
        for field in restricted_fields:
            if field in data and not is_superuser:
                raise ValidationError(
                    {field: "You do not have permission to modify this field."})
        return data

    @transaction.atomic
    def save(self, **kwargs):
        """
        Overriding save method to handle password update.
        """
        user = super().save(**kwargs)
        if password := self.validated_data.get('password', None):
            user.set_password(password)
            user.save()
        return user


class ProfilePublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "document",
            "document_type",
            "phone",
            "address",
            "is_available")


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
            raise ValidationError("Invalid credentials")
        user = None
        if email:
            user = User.objects.filter(email=email).first()
        elif document:
            user = User.objects.filter(profile__document=document).first()
        if user is None or not user.check_password(password):
            raise ValidationError("Invalid credentials.")
        attrs["user"] = user
        return attrs
