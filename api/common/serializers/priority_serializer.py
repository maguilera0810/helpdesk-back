# .\api\common\serializers\priority_serializer.py
from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.common.models import Priority


class PrioritySerializer(BaseSerializer):

    class Meta:
        model = Priority
        fields = "__all__"

    @transaction.atomic
    def save(self, **kwargs):
        return super().save(**kwargs)
