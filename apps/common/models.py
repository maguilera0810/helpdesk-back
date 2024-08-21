# .\apps\common\models.py
from typing import Union

from django.db import models

from apps.management.models import BaseInfoModel, BaseModel
from resources.enums import CategoryTypeEnum


class Tag(BaseInfoModel):
    ...


class Category(BaseInfoModel):

    code = models.CharField(max_length=41, editable=False, blank=False,
                            db_index=True,  unique=True)
    type = models.CharField(max_length=30, choices=CategoryTypeEnum.choices,
                            default=CategoryTypeEnum.SKILL)


class Skill(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profiles = models.ManyToManyField("common.Skill", related_name="skills")

    def __str__(self):
        return self.name


MODELS = [
    Skill,
]
MODEL_TYPES = Union[
    Skill,
]
