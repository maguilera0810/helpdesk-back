# .\api\authentication\views\user_view.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.authentication.serializers.auth_serializers import \
    UserPublicSerializer
from api.authentication.serializers.user_serializer import UserLightSerializer
# from api.authentication.services.auth_service import AuthService
from api.authentication.services.user_service import UserService
from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import (ApiKeyPermissionView,
                                                 BasePermissionView,
                                                 IsAdminView,
                                                 IsAuthenticatedView)
from apps.authentication.dtos import AuthDTO, map_user_data
from resources.decorators.swagger_decorators import custom_swagger_schema
from resources.utils.filter_util import FilterUtil


class UserView(BaseCRUDView):
    srv_class: type[UserService] = UserService
    serial_class: type[UserPublicSerializer] = UserPublicSerializer
    schema = custom_swagger_schema(serial_class)

    @schema(action="list")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @custom_swagger_schema(UserLightSerializer)(action="list")
    def list_light(self, request, *args, **kwargs):
        kwargs["custom_serializer"] = UserLightSerializer
        return super().list(request, *args, **kwargs)

    @schema(action="retrieve")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @schema(action="create")
    def create(self, request, *args, **kwargs):
        """
        Method: POST
        {
            'email': 'mauricio+0001@gmail.com',
            'username': 'mauricio+0001@gmail.com',
            'first_name': 'Mauricio 0001',
            'last_name': 'Aguilera',
            'is_staff': True,
            'is_active': True,
            'is_superuser': True,
            'date_joined': '2024-07-14T18:34:04.175020Z',
            'last_login': '2024-08-04T20:26:23.226225Z',
            'groups': [],
            'user_permissions': [],
            'profile': {
                'id': 2,
                'phone': '1234567890',
                'address': '',
                'document_type': 'dni',
                'document': '0000000001',
                'is_available': True,
                'user': 2
            },
        }
        """

        data = request.data
        errors, user = self.srv_class.create(data=data,
                                             request=request)
        if user:
            serializer = self.serial_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_code": errors})

    @schema(action="update")
    def update(self, request, id: int, *args, **kwargs):
        """
        Method: PUT
        {
            'id': 2,
            'last_login': '2024-08-04T20:26:23.226225Z',
            'is_superuser': True,
            'username': 'mauricio+0001@gmail.com',
            'first_name': 'Mauricio 0001',
            'last_name': 'Aguilera',
            'email': 'mauricio+0001@gmail.com',
            'is_staff': True,
            'is_active': True,
            'date_joined': '2024-07-14T18:34:04.175020Z',
            'groups': [],
            'user_permissions': [],
            'profile': {
                'id': 2,
                'phone': '1234567890',
                'address': '',
                'document_type': 'dni',
                'document': '0000000001',
                'is_available': True,
                'user': 2
            },
        }
        """
        data = request.data
        errors, user = self.srv_class.update(id=id,
                                             data=data,
                                             request=request)
        if user:
            serializer = self.serial_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    @schema(action="destroy")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @schema(action="get_user_info",
            description="Retrieve user information throw a given token",
            responses={status.HTTP_200_OK: serial_class})
    def get_user_info(self, request, *args, **kwargs):
        """
        Method: GET
        """
        user = request.user
        serializer = self.serial_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
