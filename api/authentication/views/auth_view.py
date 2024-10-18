# .\api\authentication\views\auth_view.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.authentication.serializers.auth_serializers import (
    CustomAuthTokenSerializer, UserPublicSerializer)
from api.authentication.services.auth_service import AuthService
from api.core.views.base_permission_view import ApiKeyPermissionView


class AuthApiKeyView(ApiKeyPermissionView):
    srv_class: type[AuthService] = AuthService
    serial_class: type[UserPublicSerializer] = UserPublicSerializer

    def signup(self, request, *args, **kwargs):
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
