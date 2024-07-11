# .\api\authentication\views\auth_view.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from api.authentication.serializers.auth_serializers import (
    CustomAuthTokenSerializer, UserPublicSerializer)
from api.authentication.services.auth_service import AuthService
from api.core.views.base_permission_view import (ApiKeyPermissionView,
                                                 BasePermissionView,
                                                 IsAuthenticatedView)
from apps.authentication.dtos import AuthDTO


class AuthDetailView(IsAuthenticatedView):

    def get_user_info(self, request):
        """
        Method: GET
        """
        user = request.user
        serializer = UserPublicSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthView(ApiKeyPermissionView):
    srv = AuthService

    def register(self, request):
        """
        Method: POST
        """
        import json
        print(json.dumps(request.data, indent=2))
        data = AuthDTO(**request.data)
        error, user = self.srv.create_user(data=data)
        if user:
            serializer = UserPublicSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_code": error})


class CustomTokenObtainPairView(BasePermissionView):

    def obtain_pair(self, request):
        serializer = CustomAuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        resp = {"refresh": str(refresh),
                "access": str(refresh.access_token)}
        return Response(resp, status=status.HTTP_200_OK)
