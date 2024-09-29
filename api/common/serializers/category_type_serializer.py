# .\api\common\serializers\category_serializer.py
from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.common.models import CategoryType


class CategoryTypeSerializer(BaseSerializer):

    class Meta:
        model = CategoryType
        fields = "__all__"

    @transaction.atomic
    def save(self, **kwargs):
        return super().save(**kwargs)
