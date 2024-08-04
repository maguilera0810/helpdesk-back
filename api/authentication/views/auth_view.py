# .\api\authentication\views\auth_view.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.authentication.serializers.auth_serializers import (
    CustomAuthTokenSerializer, UserAdminListSerializer, UserAdminSerializer,
    UserPublicSerializer)
from api.authentication.services.auth_service import AuthService
from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import (ApiKeyPermissionView,
                                                 BasePermissionView,
                                                 IsAdminView,
                                                 IsAuthenticatedView)
from apps.authentication.dtos import AuthDTO
from resources.utils.filter_util import FilterUtil


class AuthAdminView(BaseCRUDView, IsAdminView):
    srv_class: type[AuthService] = AuthService
    serial_class: type[UserAdminSerializer] = UserAdminSerializer

    def list(self, request, *args, **kwargs):
        """
        Method: POST
        """
        data = request.GET.dict()
        filters = FilterUtil.get_list_filters(data=data)
        items = self.srv_class.get_all(**filters)
        different_serializer = UserAdminListSerializer(items, many=True)
        return Response(different_serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Method: POST
        """
        data = AuthDTO(**request.data)
        error, user = self.srv_class.create_user(data=data)
        if user:
            serializer = self.serial_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_code": error})

    def update(self, request, id: int, *args, **kwargs):
        """
        Method: POST
        """
        data = AuthDTO(**request.data)
        error, user = self.srv_class.update_user(id=id,
                                                 data=data)
        if user:
            serializer = self.serial_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_code": error})

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
    serial_class: type[UserAdminSerializer] = UserAdminSerializer

    def create(self, request, *args, **kwargs):
        """
        Method: POST
        """
        print(request.data)
        data = AuthDTO(**request.data)
        error, user = self.srv_class.create_user(data=data)
        if user:
            serializer = self.serial_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_code": error})


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
