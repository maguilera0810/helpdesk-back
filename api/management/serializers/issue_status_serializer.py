# .\api\management\serializers\issue_status_serializer.py
from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.management.models import IssueStatus


class IssueStatusSerializer(BaseSerializer):

    class Meta:
        model = IssueStatus
        fields = "__all__"

    @transaction.atomic
    def save(self, **kwargs):
        return super().save(**kwargs)
