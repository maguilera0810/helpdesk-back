from api.core.services.base_crud_service import BaseCRUDService
from apps.management.models import Request


class RequestService(BaseCRUDService):
    model = Request
