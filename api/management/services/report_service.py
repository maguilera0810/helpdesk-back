from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import Issue


class IssueService(BaseCRUDService):
    model = Issue
