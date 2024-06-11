from abc import ABC, abstractmethod


class BaseStorageGateway(ABC):
    _instance = None

    @abstractmethod
    def upload_file(self, file, key: str):
        ...

    @abstractmethod
    def delete_file(self, key: str):
        ...

    @abstractmethod
    def delete_folder(self, key: str):
        ...

    def upload_file_cache(self, file, key: str):
        ...

    def create_folder(self, key: str):
        ...

    def download_file(self, key: str, local_path: str):
        ...
