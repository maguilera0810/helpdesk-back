# .\api\common\services\priority_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.common.models import Priority


class PriorityService(BaseCRUDService):
    model = Priority
