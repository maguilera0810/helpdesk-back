from django.conf import settings

from resources.gateways.storage import BaseStorageGateway, S3Gateway

MAIN_PROVIDER = settings.MAIN_STORAGE_PROVIDER


class StorageFactory:
    @staticmethod
    def get_provider(provider: str = MAIN_PROVIDER) -> BaseStorageGateway:
        if provider == "s3":
            return S3Gateway()
        else:
            raise ValueError(f"Unsupported storage service: {provider}")
