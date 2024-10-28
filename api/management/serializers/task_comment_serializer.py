# .\api\management\serializers\task_serializer.py
from django.db import transaction

from api.authentication.serializers.user_serializer import UserLightSerializer
from api.core.serializers.base_serializer import BaseSerializer
from apps.management.models import TaskComment


class TaskCommentSerializer(BaseSerializer):
    created_by = UserLightSerializer()

    class Meta:
        model = TaskComment
        fields = "__all__"
        read_only_fields = (
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
