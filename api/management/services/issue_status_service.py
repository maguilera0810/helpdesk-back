# .\api\management\services\plan_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import IssueStatus


class IssueStatusService(BaseCRUDService):
    model = IssueStatus
