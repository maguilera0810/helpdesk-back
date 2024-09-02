# .\api\management\services\requesting_unit_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import RequestingUnit


class RequestingUnitService(BaseCRUDService):
    model = RequestingUnit
