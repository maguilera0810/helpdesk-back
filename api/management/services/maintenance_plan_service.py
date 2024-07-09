from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import MaintenancePlan


class MaintenancePlanService(BaseCRUDService):
    model = MaintenancePlan
