# .\apps\core\models.py
from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from apps import MODEL_USER
from apps.core.validators import color_validator
from resources.enums import StoragePathEnum

ENV = settings.ENV


class BaseModel(models.Model):

    class Meta:
        abstract = True


class AuditModel(BaseModel):
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


class PeriodDateModel(BaseModel):
    start_date = models.DateField(blank=True, null=True, db_index=True)
    end_date = models.DateField(blank=True, null=True, db_index=True)

    class Meta:
        abstract = True


class PeriodDateTimeModel(BaseModel):
    start_at = models.DateTimeField(blank=True, null=True, db_index=True)
    end_at = models.DateTimeField(blank=True, null=True, db_index=True)

    class Meta:
        abstract = True


class ColorModel(BaseModel):
    color = models.CharField(max_length=7,
                             validators=[color_validator],
                             help_text="Formato hexadecimal (ej. #FF00AA)")

    class Meta:
        abstract = True


class OrderModel(BaseModel):
    order = models.SmallIntegerField(unique=True)

    class Meta:
        abstract = True


class BaseInfoModel(BaseModel):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True


class StorageModel(BaseModel):
    class Meta:
        abstract = True

    @classmethod
    def get_key(cls):
        return cls.__name__.lower()

    def get_path_storage(self, key: str = "", sufix: str = "") -> str | None:
        key = key or self.__class__.__name__.lower()
        attr = key + sufix
        if path := getattr(StoragePathEnum, attr, None):
            return path.replace("<env>", ENV).replace(f"<{key}_id>", str(self.pk))


class SlugModel(BaseModel):

    key_to_slug = "title"
    key = models.SlugField(max_length=50, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.key and (key := getattr(self, self.key_to_slug, None)):
            self.key = slugify(key)
        super().save(*args, **kwargs)


class CommentModel(BaseInfoModel, AuditModel):
    files = models.JSONField(default=list)
    created_by = models.ForeignKey(MODEL_USER, on_delete=models.DO_NOTHING,
                                   editable=False)

    class Meta:
        abstract = True


class FileModel(BaseInfoModel, AuditModel, StorageModel):
    file = models.CharField(max_length=200)
    created_by = models.ForeignKey(MODEL_USER, on_delete=models.DO_NOTHING,
                                   editable=False)

    class Meta:
        abstract = True
