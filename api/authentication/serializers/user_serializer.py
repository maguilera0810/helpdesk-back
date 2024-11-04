# .\api\authentication\serializers\user_serializer.py
from copy import deepcopy

from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.serializers import (CharField, ModelSerializer,
                                        ValidationError)

from api.core.serializers.base_serializer import BaseSerializer
from apps.authentication.models import Profile
from apps.authentication.serializers import ProfileSerializer
from resources.enums import ValidatorMsgEnum
from resources.validators.field_validator import FieldValidator


class UserLightSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
        )


class ProfileListSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "id",
            "code",
            "document",
            "phone",
            "is_available",
        )


class UserListSerializer(ModelSerializer):
    profile = ProfileListSerializer()

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


class UserPublicSerializer(ModelSerializer):
    profile = ProfileSerializer(required=False, read_only=True)

    class Meta:
        model = User
        exclude = ("password",)


class ProfileCrudSerializer(BaseSerializer):
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


class UserCrudSerializer(BaseSerializer):
    password = CharField(write_only=True, required=False)

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

    def validate_superuser(self, data: dict, request_user: User):
        if request_user.is_superuser:
            return
        if self.instance and request_user.id != self.instance.id:
            raise ValidationError(ValidatorMsgEnum.DONT_HAVE_PERMISSION)
        restricted_fields = ("is_staff", "is_active", "is_superuser")
        for field in restricted_fields:
            if field in data:
                raise ValidationError(
                    {field: ValidatorMsgEnum.DONT_HAVE_PERMISSION})

    def validate(self, data: dict):
        request_user = self.validate_request_user()
        self.validate_superuser(data=data,
                                request_user=request_user)
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
