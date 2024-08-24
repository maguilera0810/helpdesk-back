from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import IssueFile


class IssueFileService(BaseCRUDService):
    model = IssueFile
