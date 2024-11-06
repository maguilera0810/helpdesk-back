# .\api\common\serializers\tag_serializer.py
from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.common.models import Location


class LocationSerializer(BaseSerializer):

    class Meta:
        model = Location
        fields = "__all__"

    @transaction.atomic
    def save(self, **kwargs):
        return super().save(**kwargs)
