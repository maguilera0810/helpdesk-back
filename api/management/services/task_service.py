from django.contrib.auth.models import User
from django.db import transaction

from api.core.services.base_crud_service import BaseCRUDService
from api.management.serializers.task_serializer import TaskSerializer
from apps.management.models import Task


class TaskService(BaseCRUDService):
    model = Task

    def __init__(self, user: User = None) -> None:
        self.user = user

    @transaction.atomic
    def create(self, data: dict):
        """
        + title
        + description
        - code
        + type
        + status
        + priority
        + created_by: por el token de usuario
        + responsible
        + team
        + plan
        + scheduled
        // date_execution
        // interval
        - created_at
        - updated_at
        """
        serializer = TaskSerializer(data, partial=True,
                                    context={"request_user": self.user})
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors

    @transaction.atomic
    def update(self, data: dict, task_id: int, task: Task):
        task = task or self.get_one(task_id)
        serializer = TaskSerializer(instance=task, data=data,
                                    partial=True, context={"request_user": self.user})
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
