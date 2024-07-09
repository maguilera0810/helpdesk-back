# .\api\core\services\base_crud_service.py
from contextlib import suppress
from typing import Optional

from django.db import transaction

from api.core.services.base_service import BaseService
from apps.authentication.models import MODEL_TYPES as AUTH_MODEL_TYPES
from apps.common.models import MODEL_TYPES as COMMON_MODEL_TYPES
from apps.management.models import MODEL_TYPES as MANAGE_MODEL_TYPES
from resources.helpers.file_helper import FileHelper

MODEL_TYPES = AUTH_MODEL_TYPES | COMMON_MODEL_TYPES | MANAGE_MODEL_TYPES


class BaseCRUDService(BaseService):
    model: Optional[MODEL_TYPES] = None
    storage = None

    @classmethod
    def get_one(cls, id: int):
        with suppress(cls.model.DoesNotExist):
            return cls.model.objects.get(id=id)

    @classmethod
    def get_all(cls, incl_filters: dict = None, excl_filters: dict = None):
        incl_filters = incl_filters or {}
        excl_filters = excl_filters or {}
        return cls.model.objects.filter(**incl_filters).exclude(**excl_filters)

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

    @classmethod
    def create_multiple(cls, data_list: list[dict], delete_data: bool = False):
        with transaction.atomic():
            if delete_data:
                cls.delete_all()
            roulettes = [cls.model(**data) for data in data_list]
            cls.model.objects.bulk_create(roulettes)
            return roulettes

    @classmethod
    def update_files(cls, files, instance: MODEL_TYPES = None, id: int = None):
        return instance

    @classmethod
    def save_file(cls, file, instance: MODEL_TYPES, attr: str):
        if not all((hasattr(instance, attr), hasattr(instance, "get_path_storage"), getattr(cls, "storage", None))):
            return
        fh = FileHelper(file=file)
        if not (path := instance.get_path_storage(sub_key=f"_{attr}")):
            return
        path = path.replace(f"<{instance.get_key()}_id>", str(
            instance.id)).replace("<format>", fh.get_format())
        cls.storage.upload_file(file=file, key=path)
        setattr(instance, attr, f"/{path}")
        instance.save()
        return instance
