from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView

DEBUG = settings.DEBUG
TOKEN_AUTHENTICATION = settings.TOKEN_AUTHENTICATION


class BaseView(viewsets.ViewSet):
    ...


class IsAuthenticatedView(BaseView):
    """ Token Auth + Session Auth + IsAuth View Set """
    if TOKEN_AUTHENTICATION:
        permission_classes = [IsAuthenticated,]


class IsAdminView(BaseView):
    """ Token Auth + Session Auth + IsAuth + IsAdmin View Set
     It will works only when is_staff is active """
    if TOKEN_AUTHENTICATION:
        permission_classes = [IsAuthenticated, IsAdminUser,]
