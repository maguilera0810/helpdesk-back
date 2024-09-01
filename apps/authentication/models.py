# .\apps\authentication\models.py
from typing import Union

from django.db import models
from resources.enums import DocumentTypeEnum


class Profile(models.Model):

    user = models.OneToOneField("auth.User", on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=15, blank=True, db_index=True)
    address = models.CharField(max_length=255, blank=True)
    document_type = models.CharField(max_length=10, blank=False,
                                     choices=DocumentTypeEnum.choices)
    document = models.CharField(max_length=15, blank=False,
                                unique=True, db_index=True)
    is_available = models.BooleanField(default=True)


AUTH_MODELS = [
    Profile,
]
AUTH_MODEL_TYPES = Union[
    Profile,
]
