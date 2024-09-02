# .\api\authentication\services\group_service.py
from django.contrib.auth.models import Group

from api.core.services.base_crud_service import BaseCRUDService


class GroupService(BaseCRUDService):
    model = Group
