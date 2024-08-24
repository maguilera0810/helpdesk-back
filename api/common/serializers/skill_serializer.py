# .\apps\common\serializers.py
from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.common.models import Skill


class SkillSerializer(BaseSerializer):

    class Meta:
        model = Skill
        fields = "__all__"

    @transaction.atomic
    def save(self, **kwargs):
        return super().save(**kwargs)
