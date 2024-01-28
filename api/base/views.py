from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from django.conf import settings
from drf_yasg.inspectors import SwaggerAutoSchema

DEBUG = settings.DEBUG
TOKEN_AUTHENTICATION = settings.TOKEN_AUTHENTICATION


class GenericViewSet(viewsets.ViewSet):
    ...


class IsAuthenticatedView(GenericViewSet):
    """ Token Auth + Session Auth + IsAuth View Set """
    if TOKEN_AUTHENTICATION:
        permission_classes = [IsAuthenticated,]


class IsAdminViewSet(GenericViewSet):
    """ Token Auth + Session Auth + IsAuth + IsAdmin View Set
     It will works only when is_staff is active """
    if TOKEN_AUTHENTICATION:
        permission_classes = [IsAuthenticated, IsAdminUser,]
