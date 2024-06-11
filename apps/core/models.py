# .\apps\core\models.py
from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone

from resources.enums import StoragePathEnum

ENV = settings.ENV


class BaseModel(models.Model):
    class Meta:
        abstract = True


class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def time_since_created(self, format: str = "days"):
        return self.__time_since(self.created_at, format)

    def time_since_updated(self, format: str = "days"):
        return self.__time_since(self.updated_at, format)

    @classmethod
    def __time_since(cls, timestamp: datetime, format: str = "days"):
        if not timestamp:
            return
        now = timezone.now()
        delta = now - timestamp
        result = delta.days
        if format == "hours":
            result = result * 24 + (delta.seconds // 3600)
        return result


class PeriodModel(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True


class BaseInfoModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        abstract = True
