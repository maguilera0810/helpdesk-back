# .\api\common\services\skill_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.common.models import Category


class CategoryService(BaseCRUDService):
    model = Category
