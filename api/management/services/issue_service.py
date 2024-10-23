# .\api\management\services\issue_service.py
from django.contrib.auth.models import User
from django.db import transaction

from api.core.services.base_crud_service import BaseCRUDService
from api.management.serializers.task_serializer import TaskSerializer
from apps.management.models import Issue
from resources.enums import IssueStatusEnum, TaskTypeEnum


class IssueService(BaseCRUDService):
    model = Issue

    def __init__(self, user: User = None) -> None:
        self.user = user

    @transaction.atomic
    def create_task(self, id: int, request):
        """
        Params:
        id: Issue Id
        """
        issue = self.get_one(id=id)
        if not issue:
            return ["not_found"], None
        if issue.task:
            return ["task_already_created"], None
        task_data = {"id": issue.id,
                     "title": issue.title,
                     "description": issue.description,
                     "categories": issue.categories.values_list("id", flat=True),
                     "created_by": issue.created_by,
                     "type":TaskTypeEnum.EMERGENCY,
                     }
        serializer = TaskSerializer(data=task_data, partial=True,
                                    context={"request": request})
        if not serializer.is_valid():
            return serializer.errors, None
        issue.task = serializer.save()
        issue.status = IssueStatusEnum.TASK_CREATED
        issue.save()
        return None, serializer.data
