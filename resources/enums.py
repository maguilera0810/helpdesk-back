# .\resources\enums.py
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TaskPriorityEnum(TextChoices):
    highest = "highest", _("highest")
    high = "high", _("high")
    medium = "medium", _("medium")
    low = "low", _("low")
    lowest = "lowest", _("lowest")


class TaskStatusEnum(TextChoices):
    pending = "pending", _("pending")
    in_progress = "in_progress", _("in_progress")
    completed = "completed", _("completed")


class TaskTypeEnum(TextChoices):
    emergency = "emergency", _("emergency")
    preventive = "preventive", _("preventive")


class DocumentTypeEnum(TextChoices):
    id_card = "id_card", _("id_card")
    passport = "passport", _("passport")


class AuthErrorEnum(TextChoices):
    user_already_exist = "user_already_exist", _("user_already_exist")
