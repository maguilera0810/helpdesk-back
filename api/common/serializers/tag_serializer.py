# .\api\common\serializers\tag_serializer.py
from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.common.models import Tag


class TagSerializer(BaseSerializer):

    class Meta:
        model = Tag
        fields = "__all__"

    @transaction.atomic
    def save(self, **kwargs):
        return super().save(**kwargs)
