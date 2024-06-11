# .\resources\gateways\storage\__init__.py
from resources.gateways.storage.base_storage_gateway import BaseStorageGateway
from resources.gateways.storage.s3_gateway import S3Gateway


__all__ = [
    "BaseStorageGateway",
    "S3Gateway",
]
