# .\api\common\services\category_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.common.models import CategoryType


class CategoryTypeService(BaseCRUDService):
    model = CategoryType
