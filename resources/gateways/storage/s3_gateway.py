# .\resources\gateways\storage\s3_gateway.py
import boto3
from django.conf import settings

from resources.gateways.storage import BaseStorageGateway

S3_ACCESS_KEY_ID = settings.S3_ACCESS_KEY_ID
S3_ACCESS_SECRET_KEY = settings.S3_ACCESS_SECRET_KEY
BUCKET_NAME = "static.storybook-app.com"
GLOBAL_CONFIG = {"ACL": "public-read", "CacheControl": "max-age=0, public"}


class S3Gateway(BaseStorageGateway):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(S3Gateway, cls).__new__(cls)
            cls._instance.s3 = boto3.resource(
                "s3",
                aws_access_key_id=S3_ACCESS_KEY_ID,
                aws_secret_access_key=S3_ACCESS_SECRET_KEY,
            )
        return cls._instance

    def upload_file(self, file, key: str):
        if not key:
            return
        self.s3.Bucket(BUCKET_NAME).put_object(Key=key.lstrip("/"), Body=file, **GLOBAL_CONFIG)
        return True

    def upload_file_cache(self, file, key: str):
        if not key:
            return
        self.s3.Bucket(BUCKET_NAME).put_object(Key=key, Body=file, **GLOBAL_CONFIG)
        return True

    def create_folder(self, key):
        if not key:
            return
        self.s3.Bucket(BUCKET_NAME).put_object(Key=(key + "/"))
        return True

    def delete_folder(self, key: str):
        if not key:
            return
        bucket = self.s3.Bucket(BUCKET_NAME)
        objects_to_delete = bucket.objects.filter(Prefix=key.lstrip("/"))
        if delete_keys := [{"Key": obj.key} for obj in objects_to_delete]:
            bucket.delete_objects(Delete={"Objects": delete_keys})
        return True

    def delete_file(self, key):
        if not key:
            return
        self.s3.Object(BUCKET_NAME, key).delete()

    def download_file(self, key, local_path):
        if not key:
            return
        try:
            self.s3.Bucket(BUCKET_NAME).download_file(key, local_path)
            return True
        except Exception as e:
            print(f"Error al obtener el archivo de S3: {e}")
