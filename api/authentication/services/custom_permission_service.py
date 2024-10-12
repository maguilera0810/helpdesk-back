# .\api\authentication\services\permission_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.authentication.models import CustomPermission


class CustomPermissionService(BaseCRUDService):
    model = CustomPermission
