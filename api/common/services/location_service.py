# .\api\common\services\tag_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.common.models import Location


class LocationService(BaseCRUDService):
    model = Location
