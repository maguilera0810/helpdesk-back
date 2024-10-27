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
    def get_all(cls, incl_filters: dict = None, excl_filters: dict = None, order: list[str] = None):
        ...

    @classmethod
    @abstractmethod
    def delete(cls, id: int):
        ...

    @classmethod
    def delete_all(cls, incl_filters: dict = None, excl_filters: dict = None):
        ...
