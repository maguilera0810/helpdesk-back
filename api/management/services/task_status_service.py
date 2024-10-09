# .\api\management\services\plan_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import TaskStatus


class TaskStatusService(BaseCRUDService):
    model = TaskStatus
