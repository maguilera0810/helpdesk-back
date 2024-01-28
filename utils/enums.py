# .\utils\enums.py
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TaskPriority(TextChoices):
    HIGH = 'highest', _('Highest')
    HIGHEST = 'high', _('High')
    MEDIUM = 'medium', _('Medium')
    LOW = 'low', _('Low')
    LOWEST = 'lowest', _('Lowest')


class TaskStatus(TextChoices):
    PENDING = 'pending', _('Pending')
    IN_PROGRESS = 'in_progress', _('In Progress')
    COMPLETED = 'completed', _('Completed')


class TaskType(TextChoices):
    EMERGENCY = 'emergency', _('Emergency')
    PREVENTIVE = 'preventive', _('Preventive')
