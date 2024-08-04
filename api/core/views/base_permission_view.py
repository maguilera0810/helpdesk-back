# .\api\core\views\base_permission_view.py
from django.conf import settings
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.core.permissions.base_permission import ApiKeyPermission

USE_BASIC_AUTH = settings.USE_BASIC_AUTH
if USE_BASIC_AUTH:
    AUTHENTICATION_CLASSES = (BasicAuthentication,
                              JWTAuthentication)
else:
    AUTHENTICATION_CLASSES = (JWTAuthentication,)


class BasePermissionView(viewsets.ViewSet):
    permission_classes = (AllowAny,)


class ApiKeyPermissionView(BasePermissionView):
    """RequireApiKey API View"""

    permission_classes = (ApiKeyPermission,)


class IsAuthenticatedView(BasePermissionView):
    """ Token Auth + Session Auth + IsAuth View Set """
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = (IsAuthenticated,)


class IsAdminView(IsAuthenticatedView):
    """ Token Auth + Session Auth + IsAuth + IsAdmin View Set
     It will works only when is_staff is active """
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = (IsAuthenticated, IsAdminUser,)
