# .\api\management\services\issue_status_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import IssueStatus


class IssueStatusService(BaseCRUDService):
    model = IssueStatus
