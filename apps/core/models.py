# .\apps\core\models.py
from django.db import models
from django.utils import timezone


class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PeriodModel(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        abstract = True


class Model(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        abstract = True
