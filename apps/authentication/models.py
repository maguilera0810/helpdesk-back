# .\apps\authentication\models.py
from typing import Union

from django.db import models
from django.utils.text import slugify

from apps.core.models import AuditModel, BaseInfoModel, BaseModel, SlugModel
from resources.enums import DocumentTypeEnum


class Profile(BaseModel):

    user = models.OneToOneField("auth.User", on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=15, blank=True, db_index=True)
    address = models.CharField(max_length=255, blank=True)
    document_type = models.CharField(max_length=10, blank=False,
                                     choices=DocumentTypeEnum.choices)
    document = models.CharField(max_length=15, blank=False,
                                unique=True, db_index=True)
    is_available = models.BooleanField(default=True)


class Role(BaseInfoModel, SlugModel, AuditModel):

    title = models.CharField(max_length=50, unique=True)
    users = models.ManyToManyField(
        "auth.User", related_name="roles", blank=True)
    permissions = models.ManyToManyField("authentication.Permission",
                                         related_name="roles", blank=True)

    def __str__(self):
        return self.key


class Permission(BaseInfoModel, SlugModel, AuditModel):

    title = models.CharField(max_length=50, unique=True)
    group = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.key


AUTH_MODELS = [
    Profile,
    Permission,
    Role,
]
AUTH_MODEL_TYPES = Union[
    Profile,
    Permission,
    Role,
]
