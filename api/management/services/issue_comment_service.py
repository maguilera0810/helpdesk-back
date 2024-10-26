# .\api\management\services\task_comment_service.py

from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import IssueComment


class IssueCommentService(BaseCRUDService):
    model = IssueComment
