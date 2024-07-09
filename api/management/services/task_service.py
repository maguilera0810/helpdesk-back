from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import Task


class TaskService(BaseCRUDService):
    model = Task
