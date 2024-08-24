from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from azure.storage.blob import BlobServiceClient
from django.conf import settings


class AzureStorage:
    """
    Clase para manejar la subida y eliminación de archivos en Azure Blob Storage.
    """

    def __init__(self):
        self.storage = default_storage
        self.account_name = settings.AZURE_ACCOUNT_NAME
        self.account_key = settings.AZURE_ACCOUNT_KEY
        self.container = settings.AZURE_CONTAINER
        self.blob_service_client = BlobServiceClient(
            account_url=f"https://{self.account_name}.blob.core.windows.net",
            credential=self.account_key
        )

    def upload_file(self, file, filename=None):
        """
        Sube un archivo a Azure Blob Storage.

        :param file: Archivo que se va a subir. Puede ser un File o ContentFile.
        :param filename: Nombre opcional para el archivo. Si no se proporciona, se usa el nombre original del archivo.
        :return: URL del archivo subido.
        """
        if filename is None:
            filename = file.name
        path = self.storage.save(filename, ContentFile(file.read()))
        file_url = self.storage.url(path)
        return file_url

    def delete_file(self, filename):
        """
        Elimina un archivo de Azure Blob Storage.

        :param filename: Nombre del archivo a eliminar.
        """
        self.storage.delete(filename)

    def delete_folder(self, folder_name):
        """
        Elimina todos los blobs dentro de una "carpeta" (prefijo) en Azure Blob Storage.

        :param folder_name: Nombre del prefijo o "carpeta" a eliminar.
        """
        container_client = self.blob_service_client.get_container_client(
            self.container)
        blobs = container_client.list_blobs(name_starts_with=folder_name)
        for blob in blobs:
            blob_name = blob.name
            container_client.delete_blob(blob_name)
