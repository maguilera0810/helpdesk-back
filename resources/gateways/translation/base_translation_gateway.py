# .\resources\gateways\translation\base_translation_gateway.py
from abc import ABC, abstractmethod


class BaseTranslationGateway(ABC):
    @abstractmethod
    def add_key(self, key: str, translation: str) -> bool:
        ...

    @abstractmethod
    def delete_key(self, key: str):
        ...

    @abstractmethod
    def fetch_translation(self, key: str, lang: str):
        ...

    def update_key_labels(self, key: str, labels: list[str]):
        ...

    def update_translation(self, key_id: int, target: str):
        ...

    def create_translations_files(self):
        ...
