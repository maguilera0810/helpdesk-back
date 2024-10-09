# .\apps\common\models.py
from typing import Union

from django.db import models

from apps.common.validators import color_validator
from apps.management.models import BaseInfoModel


class Tag(BaseInfoModel):

    code = models.CharField(max_length=35, editable=False, blank=False,
                            db_index=True,  unique=True, help_text="max_length= len(model_name) + 33")
    color = models.CharField(max_length=7,
                             validators=[color_validator],
                             help_text="Formato hexadecimal (ej. #FF00AA)")


class CategoryType(BaseInfoModel):
    ...


class Category(BaseInfoModel):

    code = models.CharField(max_length=41, editable=False, blank=False,
                            db_index=True,  unique=True, help_text="max_length= len(model_name) + 33")
    type = models.ForeignKey("common.CategoryType", null=True,
                             on_delete=models.DO_NOTHING)
    relations = models.ManyToManyField("common.Category", blank=True)
    color = models.CharField(max_length=7,
                             validators=[color_validator],
                             help_text="Formato hexadecimal (ej. #FF00AA)")


class Skill(BaseInfoModel):

    code = models.CharField(max_length=37, editable=False, blank=False,
                            db_index=True,  unique=True, help_text="max_length= len(model_name) + 33")
    profiles = models.ManyToManyField("common.Skill", related_name="skills")


class Priority(BaseInfoModel):
    ...
    icon = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=7,
                             validators=[color_validator],
                             help_text="Formato hexadecimal (ej. #FF00AA)")


COMMON_MODELS = [
    Category,
    Skill,
    Tag,
]
COMMON_MODEL_TYPES = Union[
    Category,
    Skill,
    Tag,
]
