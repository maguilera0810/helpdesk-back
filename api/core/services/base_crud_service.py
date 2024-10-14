# .\api\core\services\base_crud_service.py
from contextlib import suppress
from typing import Optional

from django.db import transaction

from api.core.services.base_service import BaseService
from apps.authentication.models import AUTH_MODEL_TYPES
from apps.common.models import COMMON_MODEL_TYPES
from apps.core.models import OrderModel
from apps.management.models import MANAGEMENT_MODEL_TYPES
from resources.helpers.file_helper import FileHelper

ALL_MODEL_TYPES = AUTH_MODEL_TYPES | COMMON_MODEL_TYPES | MANAGEMENT_MODEL_TYPES


class BaseCRUDService(BaseService):
    model: Optional[ALL_MODEL_TYPES] = None
    storage = None

    @classmethod
    def get_one(cls, id: int):
        with suppress(cls.model.DoesNotExist):
            return cls.model.objects.get(id=id)

    @classmethod
    def get_all(cls, incl_filters: dict = None, excl_filters: dict = None):
        incl_filters = incl_filters or {}
        excl_filters = excl_filters or {}
        query = (cls.model.objects.filter(**incl_filters)
                 .exclude(**excl_filters))
        if issubclass(cls.model, OrderModel):
            query = query.order_by("order")
        return query

    @classmethod
    def delete(cls, id: int):
        with suppress(cls.model.DoesNotExist):
            instance = cls.model.objects.get(id=id)
            instance.delete()
            return True

    @classmethod
    def delete_all(cls, incl_filters: dict = None, excl_filters: dict = None):
        cls.get_all(incl_filters=incl_filters,
                    excl_filters=excl_filters).delete()
