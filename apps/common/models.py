# .\apps\common\models.py
from typing import Union

from django.core.validators import RegexValidator
from django.db import models

from apps.common.validators import color_validator
from apps.management.models import BaseInfoModel, BaseModel
from resources.enums import CategoryTypeEnum


class Tag(BaseInfoModel):

    code = models.CharField(max_length=35, editable=False, blank=False,
                            db_index=True,  unique=True)
    color = models.CharField(max_length=7,
                             validators=[color_validator],
                             help_text="Formato hexadecimal (ej. #FF00AA)")


class Category(BaseInfoModel):

    code = models.CharField(max_length=41, editable=False, blank=False,
                            db_index=True,  unique=True)
    type = models.CharField(max_length=30, choices=CategoryTypeEnum.choices,
                            default=CategoryTypeEnum.SKILL)
    relations = models.ManyToManyField("common.Category", blank=True)
    color = models.CharField(max_length=7,
                             validators=[color_validator],
                             help_text="Formato hexadecimal (ej. #FF00AA)")


class Skill(BaseInfoModel):

    code = models.CharField(max_length=37, editable=False, blank=False,
                            db_index=True,  unique=True)
    profiles = models.ManyToManyField("common.Skill", related_name="skills")

    def __str__(self):
        return self.name


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
