# .\api\management\services\task_history_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import TaskIssueLocation


class TaskIssueLocationService(BaseCRUDService):
    model = TaskIssueLocation
