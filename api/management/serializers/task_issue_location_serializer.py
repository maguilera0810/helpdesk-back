# .\api\management\serializers\task_serializer.py
from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.management.models import TaskIssueLocation


class TaskIssueLocationSerializer(BaseSerializer):

    class Meta:
        model = TaskIssueLocation
        fields = "__all__"

    @transaction.atomic
    def save(self, **kwargs):
        return super().save(**kwargs)
