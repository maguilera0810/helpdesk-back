from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.management.models import Task


class TaskSerializer(BaseSerializer):

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
