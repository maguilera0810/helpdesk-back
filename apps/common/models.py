# .\apps\common\models.py
from typing import Union

from django.db import models

from apps.common.validators import color_validator
from apps.core.models import BaseInfoModel, ColorModel, OrderModel


class Tag(BaseInfoModel, ColorModel):

    code = models.CharField(max_length=35, editable=False, blank=False,
                            db_index=True,  unique=True, help_text="max_length= len(model_name) + 33")


class CategoryType(BaseInfoModel):
    ...


class Category(BaseInfoModel, ColorModel):

    code = models.CharField(max_length=41, editable=False, blank=False,
                            db_index=True,  unique=True, help_text="max_length= len(model_name) + 33")
    type = models.ForeignKey("common.CategoryType", null=True,
                             on_delete=models.DO_NOTHING)
    relations = models.ManyToManyField("common.Category", blank=True)


class Skill(BaseInfoModel):

    code = models.CharField(max_length=37, editable=False, blank=False,
                            db_index=True,  unique=True, help_text="max_length= len(model_name) + 33")
    profiles = models.ManyToManyField("common.Skill", related_name="skills")


class Priority(BaseInfoModel, ColorModel, OrderModel):

    icon = models.TextField(blank=True)
    group = models.CharField(max_length=50, blank=True)


COMMON_MODELS = [
    Category,
    Priority,
    Skill,
    Tag,
]
COMMON_MODEL_TYPES = Union[
    Category,
    Priority,
    Skill,
    Tag,
]
