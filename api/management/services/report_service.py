from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import Report


class ReportService(BaseCRUDService):
    model = Report
