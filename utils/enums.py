# .\utils\enums.py
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TaskPriority(TextChoices):
    HIGH = 'highest', _('highest')
    HIGHEST = 'high', _('high')
    MEDIUM = 'medium', _('medium')
    LOW = 'low', _('low')
    LOWEST = 'lowest', _('lowest')


class TaskStatus(TextChoices):
    PENDING = 'pending', _('pending')
    IN_PROGRESS = 'in_progress', _('in_progress')
    COMPLETED = 'completed', _('completed')


class TaskType(TextChoices):
    EMERGENCY = 'emergency', _('emergency')
    PREVENTIVE = 'preventive', _('preventive')
