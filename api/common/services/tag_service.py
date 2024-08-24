# .\api\common\services\tag_service.py
from api.core.services.base_crud_service import BaseCRUDService
from apps.common.models import Tag


class TagService(BaseCRUDService):
    model = Tag
