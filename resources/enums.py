from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


class TaskPriorityEnum(TextChoices):
    HIGHEST = "highest", _("highest")
    HIGH = "high", _("high")
    MEDIUM = "medium", _("medium")
    LOW = "low", _("low")
    LOWEST = "lowest", _("lowest")


class TaskStatusEnum(TextChoices):
    PENDING = "pending", _("pending")
    IN_PROGRESS = "in_progress", _("in_progress")
    COMPLETED = "completed", _("completed")


class TaskTypeEnum(TextChoices):
    EMERGENCY = "emergency", _("emergency")
    PREVENTIVE = "preventive", _("preventive")


class DocumentTypeEnum(TextChoices):
    ID_CARD = "id_card", _("id_card")
    PASSPORT = "passport", _("passport")


class AuthErrorEnum(TextChoices):
    USER_ALREADY_EXIST = "user_already_exist", _("user_already_exist")
    USER_DOES_NOT_EXIST = "user_does_not_exist", _("user_does_not_exist")
    EMAIL_ALREADY_EXIST = "email_already_exist", _("email_already_exist")
    DOCUMENT_ALREADY_EXIST = "document_already_exist", _(
        "document_already_exist")


class ValidatorErrorEnum(TextChoices):
    EMAIL_ERROR = "email_error", _("email_error")
    PASSWORD_LENGTH_ERROR = "password_length_error", _("password_length_error")
    PASSWORD_UPPERCASE_ERROR = "password_uppercase_error", _(
        "password_uppercase_error")
    PASSWORD_LOWERCASE_ERROR = "password_lowercase_error", _(
        "password_lowercase_error")
    PASSWORD_NUMBER_ERROR = "password_number_error", _("password_number_error")
    PASSWORD_SPECIAL_CHAR_ERROR = "password_special_char_error", _(
        "password_special_char_error")
    PHONE_ERROR = "phone_error", _("phone_error")
