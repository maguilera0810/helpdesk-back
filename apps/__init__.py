# .\apps\__init__.py
from apps.authentication.models import MODEL_TYPES as AUTH_MODEL_TYPES
from apps.common.models import MODEL_TYPES as COMMON_MODEL_TYPES
from apps.management.models import MODEL_TYPES as MANAGE_MODEL_TYPES

MODEL_TYPES = AUTH_MODEL_TYPES | COMMON_MODEL_TYPES | MANAGE_MODEL_TYPES


__all__ = ["MODEL_TYPES"]
