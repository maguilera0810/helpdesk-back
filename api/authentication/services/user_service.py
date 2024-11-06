# .\api\authentication\services\user_service.py
from dataclasses import asdict

from django.contrib.auth.models import User
from django.db import transaction

from api.authentication.serializers.auth_serializers import (
    ProfileCrudSerializer, UserCrudSerializer)
from api.core.services.base_crud_service import BaseCRUDService
from apps.authentication.models import Profile
from resources.enums import ValidatorMsgEnum


class UserService(BaseCRUDService):
    model = User

    @classmethod
    @transaction.atomic
    def create(cls, data: dict, request):

        user_serializer = UserCrudSerializer(data=data,
                                             partial=True,
                                             context={'request': request})
        if not user_serializer.is_valid():
            return user_serializer.errors, None
        user = user_serializer.save()
        if profile_data := data.pop("profile", None):
            profile_data["user"] = user.id
            profile_serializer = ProfileCrudSerializer(data=profile_data,
                                                       partial=True)
            if not profile_serializer.is_valid():
                return profile_serializer.errors, None
            profile_serializer.save()
        return [], user

    @classmethod
    @transaction.atomic
    def update(cls, id: int, data: dict, request):
        """
        Updates a user and their profile information.

        Args:
            id (int): The ID of the user to update.
            data (dict): The data transfer object containing the new user data.
            request (http request):

        Returns:
            tuple: A tuple containing a list of error messages (if any) and the updated user instance.
        """
        user = User.objects.filter(id=id).first()
        if not user:
            return [ValidatorMsgEnum.USER_DOES_NOT_EXIST], None
        profile_data = data.pop("profile", None)
        context = {"request": request}
        user_serializer = UserCrudSerializer(instance=user,
                                             data=data,
                                             partial=True,
                                             context=context)
        if not user_serializer.is_valid():
            return user_serializer.errors, None
        user = user_serializer.save()
        if profile_data:
            profile_serializer = ProfileCrudSerializer(instance=user.profile,
                                                       data=profile_data,
                                                       context=context,
                                                       partial=True)
            if not profile_serializer.is_valid():
                return profile_serializer.errors, None
            profile_serializer.save()
        return [], user

    @classmethod
    @transaction.atomic
    def update_password(cls, id: int, data: dict):
        """
        Updates the password for a given user.

        Args:
            id (int): The ID of the user to update.
            data (dict): The data transfer object containing the new password.

        Returns:
            tuple: A tuple containing a list of error messages (if any) and the updated user instance.
        """
        user = User.objects.filter(id=id).first()
        if not user:
            return [ValidatorMsgEnum.USER_DOES_NOT_EXIST], None

        password_data = {"password": data["password"]}
        serializer = UserCrudSerializer(instance=user,
                                        data=password_data,
                                        partial=True)
        if not serializer.is_valid():
            return serializer.errors, None

        user = serializer.save()
        return [], user

    @classmethod
    @transaction.atomic
    def delete_user(cls, id: int, request: User):
        """
        Deletes a user and their profile information.

        Args:
            id (int): The ID of the user to delete.
            request (User): The user making the request.

        Returns:
            tuple: A tuple containing a success message or error message.
        """
        # Verificar si el usuario que realiza la solicitud tiene permisos
        if not request.is_superuser:
            return ["You do not have permission to delete this user."], None

        # Buscar el usuario por ID
        user = User.objects.filter(id=id).first()
        if not user:
            return [ValidatorMsgEnum.USER_DOES_NOT_EXIST], None

        # Eliminar el perfil y el usuario
        profile = user.profile
        profile.delete()
        user.delete()
        return ["User and profile deleted successfully"], True
