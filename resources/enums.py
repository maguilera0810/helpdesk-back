from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TaskPriorityEnum(TextChoices):
    HIGHEST = "highest", _("highest")
    HIGH = "high", _("high")
    MEDIUM = "medium", _("medium")
    LOW = "low", _("low")
    LOWEST = "lowest", _("lowest")


class TaskStatusEnum(TextChoices):
    TO_DO = "to_do", _("to_do")
    IN_PROGRESS = "in_progress", _("in_progress")
    BLOCKED = "blocked", _("blocked")
    COMPLETED = "completed", _("completed")


class TaskTypeEnum(TextChoices):
    EMERGENCY = "emergency", _("emergency")
    PREVENTIVE = "preventive", _("preventive")


class DocumentTypeEnum(TextChoices):
    DNI = "dni", _("dni")
    PASSPORT = "passport", _("passport")


class ValidatorMsgEnum(TextChoices):
    USER_ALREADY_EXIST = "user_already_exist", _("user_already_exist")
    USER_DOES_NOT_EXIST = "user_does_not_exist", _("user_does_not_exist")
    EMAIL_ERROR = "email_error", _("email_error")
    EMAIL_ALREADY_EXIST = "email_already_exist", _("email_already_exist")
    EMAIL_OK = "email_ok", _("email_ok")
    DOCUMENT_ALREADY_EXIST = "document_already_exist", _(
        "document_already_exist")
    DOCUMENT_OK = "document_ok", _("document_ok")
    DONT_HAVE_PERMISSION = "dont_have_permission", _("dont_have_permission")
    PASSWORD_LENGTH_ERROR = "password_length_error", _("password_length_error")
    PASSWORD_UPPERCASE_ERROR = "password_uppercase_error", _(
        "password_uppercase_error")
    PASSWORD_LOWERCASE_ERROR = "password_lowercase_error", _(
        "password_lowercase_error")
    PASSWORD_NUMBER_ERROR = "password_number_error", _("password_number_error")
    PASSWORD_MATCH_ERROR = "password_match_error", _("password_match_error")
    PASSWORD_SPECIAL_CHAR_ERROR = "password_special_char_error", _(
        "password_special_char_error")
    PASSWORD_REQUIRED = "password_required", _("password_required")
    PASSWORD_OK = "password_ok", _("password_ok")
    PHONE_ERROR = "phone_error", _("phone_error")
    PHONE_OK = "phone_ok", _("phone_ok")
    ALL_OK = "all_ok", _("all_ok")
