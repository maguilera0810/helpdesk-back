# .\apps\authentication\models.py
from typing import Union

from django.db import models
from resources.enums import DocumentTypeEnum


class Profile(models.Model):

    user = models.OneToOneField("auth.User", on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    document_type = models.CharField(max_length=10, blank=False,
                                     choices=DocumentTypeEnum.choices)
    document = models.CharField(max_length=15, blank=False)
    is_available = models.BooleanField(default=True)
    external_code = models.CharField(max_length=50, blank=True)


MODELS = [
    Profile,
]
MODEL_TYPES = Union[
    Profile,
]
