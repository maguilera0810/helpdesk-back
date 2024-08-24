# DOCUMENTACION:
# https://diegoamorin.com/django-signals/
# https://docs.djangoproject.com/en/4.2/topics/signals/

from django.db.models import Model
from django.db.models.signals import pre_save

from apps.management.models import Task
from resources.decorators import register_receivers
from resources.utils.decode_util import DecodeUtil


@register_receivers(pre_save, (Task,))
def set_default_code(sender, instance, **kwargs) -> None:
    if not instance.pk and hasattr(instance, "code") and not instance.code:
        instance.code = DecodeUtil.generate_default_string(sender.__name__)
