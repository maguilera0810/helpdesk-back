from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import Plan


class PlanService(BaseCRUDService):
    model = Plan
