# .\api\management\serializers\task_serializer.py
from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.management.models import Task
from rest_framework.serializers import PrimaryKeyRelatedField


class TaskSerializer(BaseSerializer):
    issue = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = (
            "code",
            "created_by",
            "created_at",
            "updated_at",
        )

    @transaction.atomic
    def save(self, **kwargs):

        if not self.instance:
            request = self.context.get("request")
            self.validated_data["created_by"] = request.user
        return super().save(**kwargs)
