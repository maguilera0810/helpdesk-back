# .\api\authentication\views\auth_view.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.authentication.serializers.auth_serializers import (
    CustomAuthTokenSerializer, UserPublicSerializer)
from api.authentication.services.auth_service import AuthService
from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import (ApiKeyPermissionView,
                                                 BasePermissionView,
                                                 IsAdminView,
                                                 IsAuthenticatedView)
from apps.authentication.dtos import AuthDTO, map_user_data
from resources.utils.filter_util import FilterUtil


class AuthAdminView(BaseCRUDView, IsAdminView):
    srv_class: type[AuthService] = AuthService
    serial_class: type[UserPublicSerializer] = UserPublicSerializer

    def list(self, request, *args, **kwargs):
        """
        Method: GET
        """
        data = request.GET.dict()
        filters = FilterUtil.get_list_filters(data=data)
        items = self.srv_class.get_all(**filters)
        different_serializer = UserPublicSerializer(items, many=True)
        return Response(different_serializer.data, status=status.HTTP_200_OK)

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
        errors, user = self.srv_class.create_user(data=data,
                                                  request=request)
        if user:
            serializer = self.serial_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_code": errors})

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
        errors, user = self.srv_class.update_user(id=id,
                                                  data=data,
                                                  request=request)
        if user:
            serializer = self.serial_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id: int, *args, **kwargs):
        """
        Method: DELETE
        """
        if self.srv_class.delete_user(id=id):
            return Response(True, status=status.HTTP_200_OK)
        return Response(False, status=status.HTTP_400_BAD_REQUEST)


class AuthDetailView(IsAuthenticatedView):
    serial_class: type[UserPublicSerializer] = UserPublicSerializer

    def get_user_info(self, request, *args, **kwargs):
        """
        Method: GET
        """
        user = request.user
        serializer = self.serial_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthView(ApiKeyPermissionView):
    srv_class: type[AuthService] = AuthService
    serial_class: type[UserPublicSerializer] = UserPublicSerializer

    def create(self, request, *args, **kwargs):
        """
        Method: POST
        """
        data = request.data
        error, user = self.srv_class.create_user(data=data)
        if user:
            serializer = self.serial_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_code": error}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(ApiKeyPermissionView):

    def obtain_pair(self, request):
        serializer = CustomAuthTokenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        resp = {"refresh": str(refresh),
                "access": str(refresh.access_token)}
        return Response(resp, status=status.HTTP_200_OK)
