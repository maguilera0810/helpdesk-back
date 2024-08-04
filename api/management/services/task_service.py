from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import Task
from django.db import transaction
from django.contrib.auth.models import User
from apps.authentication.dtos import AuthDTO


class TaskService(BaseCRUDService):
    model = Task

    @classmethod
    @transaction.atomic
    def create_task(cls, user: User, data):
        ...
