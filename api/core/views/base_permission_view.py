from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from api.core.permissions.base_permission import ApiKeyPermission

DEBUG = settings.DEBUG
TOKEN_AUTHENTICATION = settings.TOKEN_AUTHENTICATION


class BasePermissionView(viewsets.ViewSet):
    ...


class ApiKeyPermissionView(BasePermissionView):
    """RequireApiKey API View"""

    permission_classes = (ApiKeyPermission,)


class IsAuthenticatedView(BasePermissionView):
    """ Token Auth + Session Auth + IsAuth View Set """
    if TOKEN_AUTHENTICATION:
        permission_classes = [IsAuthenticated,]


class IsAdminView(BasePermissionView):
    """ Token Auth + Session Auth + IsAuth + IsAdmin View Set
     It will works only when is_staff is active """
    if TOKEN_AUTHENTICATION:
        permission_classes = [IsAuthenticated, IsAdminUser,]
