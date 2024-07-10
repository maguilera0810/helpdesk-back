# .\apps\common\models.py
from collections.abc import Iterable
from typing import Union

from django.db import models

# class Tag(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name


class Skill(models.Model):
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
