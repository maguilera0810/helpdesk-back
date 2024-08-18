from django.db import transaction
from rest_framework.serializers import ModelSerializer, ValidationError

from apps.management.models import Task


class TaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = (
            "code",
            "created_by",
        )

    def validate_responsible(self, value):
        team_members = self.initial_data.get("team", [])
        if value and value.id not in team_members:
            raise ValidationError(
                "The responsible person must be part of the assigned team.")
        return value

    @transaction.atomic
    def save(self, **kwargs):

        request_user = self.context.get("request_user")

        if self.instance:
            for param in ("code", "created_by"):
                if param in self.validated_data:
                    self.validated_data.pop(param)
        else:
            self.validated_data["created_by"] = request_user
        return super().save(**kwargs)
