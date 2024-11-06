# .\apps\common\models.py
from typing import Union

from django.db import models

from apps.core.models import AuditModel, BaseInfoModel, ColorModel, OrderModel

code_help_text = "max_length= len(model_nadme) + 33"


class Tag(BaseInfoModel, ColorModel):

    code = models.CharField(max_length=35, editable=False, blank=False,
                            db_index=True,  unique=True, help_text=code_help_text)


class CategoryType(BaseInfoModel):
    ...


class Category(BaseInfoModel, ColorModel):

    code = models.CharField(max_length=41, editable=False, blank=False,
                            db_index=True,  unique=True, help_text=code_help_text)
    type = models.ForeignKey("common.CategoryType", null=True,
                             on_delete=models.DO_NOTHING)
    relations = models.ManyToManyField("common.Category", blank=True)


class Skill(BaseInfoModel):

    code = models.CharField(max_length=37, editable=False, blank=False,
                            db_index=True,  unique=True, help_text=code_help_text)
    profiles = models.ManyToManyField("common.Skill", related_name="skills")


class Priority(BaseInfoModel, ColorModel, OrderModel):

    icon = models.TextField(blank=True)


class Location(BaseInfoModel, AuditModel):

    postal_code = models.CharField(max_length=20, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True,
                              null=True, help_text="Coordenada de latitud.")
    long = models.DecimalField(max_digits=9, decimal_places=6, blank=True,
                               null=True, help_text="Coordenada de longitud.")
    address = models.CharField(max_length=255,
                               help_text="Dirección completa de la ubicación.")


COMMON_MODELS = [
    Category,
    Priority,
    Location,
    Skill,
    Tag,
]
COMMON_MODEL_TYPES = Union[
    Category,
    Priority,
    Location,
    Skill,
    Tag,
]
