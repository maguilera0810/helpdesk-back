# .\api\management\services\task_comment_service.py

from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import TaskComment


class TaskCommentService(BaseCRUDService):
    model = TaskComment
