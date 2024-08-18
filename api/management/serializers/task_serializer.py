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

    def validate_request_user(self):
        request = self.context.get("request")
        if not request:
            raise ValidationError({"request": "no_request"})
        request_user = request.user
        if not request_user:
            raise ValidationError({"user": "no_request_user"})
        return request_user

    def validate(self, data: dict):
        self.validate_request_user()
        return data

    @transaction.atomic
    def save(self, **kwargs):
        if self.instance:
            for param in ("code", "created_by"):
                if param in self.validated_data:
                    self.validated_data.pop(param)
        else:
            request = self.context.get("request")
            self.validated_data["created_by"] = request.user
        return super().save(**kwargs)
