# .\api\management\services\task_history_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import TaskHistory


class TaskHistoryService(BaseCRUDService):
    model = TaskHistory
