# .\apps\core\signals.py
# DOCUMENTACION:
# https://diegoamorin.com/django-signals/
# https://docs.djangoproject.com/en/4.2/topics/signals/

from django.db.models.signals import pre_save

from apps.authentication.models import AUTH_MODELS
from apps.common.models import COMMON_MODELS
from apps.management.models import MANAGEMENT_MODELS
from resources.decorators import register_receivers
from resources.utils.decode_util import DecodeUtil

ALL_MODELS = (
    *COMMON_MODELS,
    *MANAGEMENT_MODELS,
    *AUTH_MODELS,
)


@register_receivers(pre_save, ALL_MODELS)
def set_default_code(sender, instance, **kwargs) -> None:
    if not instance.pk and hasattr(instance, "code"):
        instance.code = DecodeUtil.generate_default_string(sender.__name__)
