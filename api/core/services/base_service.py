# .\api\core\services\base_service.py
from abc import ABC, abstractmethod

from django.db.models import Model


class BaseService(ABC):

    @classmethod
    @abstractmethod
    def get_one(cls, id: int):
        ...

    @classmethod
    @abstractmethod
    def get_all(cls, incl_filters: dict = None, excl_filters: dict = None):
        ...

    @classmethod
    @abstractmethod
    def delete(cls, id: int):
        ...

    @classmethod
    def delete_all(cls, incl_filters: dict = None, excl_filters: dict = None):
        ...

    @classmethod
    def create_multiple(cls, data_list: list, delete_data: bool = False):
        ...

    @classmethod
    def update_files(cls, files, instance: Model = None, id: int = None):
        ...

    @classmethod
    def save_file(cls, file, instance: Model, attr: str):
        ...

    @classmethod
    def set_translation_keys(
        cls,
        instance: Model = None,
        id: int = None,
        keys: list[str] = ["translation_key"],
    ):
        ...
