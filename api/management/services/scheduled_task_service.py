# .\api\management\services\scheduled_task_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import ScheduledTask


class ScheduledTaskService(BaseCRUDService):
    model = ScheduledTask
