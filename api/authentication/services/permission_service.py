# .\api\authentication\services\permission_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.authentication.models import Permission


class PermissionService(BaseCRUDService):
    model = Permission
