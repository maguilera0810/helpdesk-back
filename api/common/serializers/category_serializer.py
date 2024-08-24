from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.common.models import Category


class CategorySerializer(BaseSerializer):

    class Meta:
        model = Category
        fields = "__all__"

    @transaction.atomic
    def save(self, **kwargs):
        return super().save(**kwargs)
