from django.db import transaction

from api.core.serializers.base_serializer import BaseSerializer
from apps.management.models import IssueFile


class IssueFileSerializer(BaseSerializer):

    class Meta:
        model = IssueFile
        fields = "__all__"

    @transaction.atomic
    def save(self, **kwargs):
        if not self.instance:
            request = self.context.get("request")
            self.validated_data["created_by"] = request.user
        return super().save(**kwargs)
