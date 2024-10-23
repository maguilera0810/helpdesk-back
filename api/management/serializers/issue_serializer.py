# .\api\management\serializers\issue_serializer.py
from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.management.models import Issue


class IssueSerializer(BaseSerializer):

    class Meta:
        model = Issue
        fields = "__all__"

    @transaction.atomic
    def save(self, **kwargs):
        if not self.instance:
            request = self.context.get("request")
            self.validated_data["created_by"] = request.user
        return super().save(**kwargs)
