# .\api\core\views\base_permission_view.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.core.permissions.base_permission import ApiKeyPermission


class BasePermissionView(viewsets.ViewSet):
    permission_classes = (AllowAny,)


class ApiKeyPermissionView(BasePermissionView):
    """RequireApiKey API View"""

    permission_classes = (ApiKeyPermission,)


class IsAuthenticatedView(BasePermissionView):
    """ Token Auth + Session Auth + IsAuth View Set """
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)


class IsAdminView(IsAuthenticatedView):
    """ Token Auth + Session Auth + IsAuth + IsAdmin View Set
     It will works only when is_staff is active """
    permission_classes = (IsAuthenticated, IsAdminUser,)
