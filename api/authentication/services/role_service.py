# .\api\authentication\services\role_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.authentication.models import Role


class RoleService(BaseCRUDService):
    model = Role
