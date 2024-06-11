from django.conf import settings
from rest_framework.permissions import BasePermission

API_KEYS = settings.API_KEYS


class ApiKeyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get("API-KEY") in API_KEYS
