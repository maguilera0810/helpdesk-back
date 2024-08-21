from django.db import transaction
from rest_framework.serializers import ModelSerializer, ValidationError

from apps.management.models import Issue


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = "__all__"
        # read_only_fields = ()

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

        if not self.instance:
            request = self.context.get("request")
            self.validated_data["created_by"] = request.user
        return super().save(**kwargs)
