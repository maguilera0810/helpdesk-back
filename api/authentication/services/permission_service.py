# .\api\authentication\services\permission_service.py
from django.contrib.auth.models import Permission

from api.core.services.base_crud_service import BaseCRUDService


class PermissionService(BaseCRUDService):
    model = Permission
