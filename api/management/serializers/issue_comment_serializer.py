# .\api\management\serializers\issue_comment_serializer.py
from django.db import transaction

from api.authentication.serializers.user_serializer import UserLightSerializer
from api.core.serializers.base_serializer import BaseSerializer
from apps.management.models import IssueComment


class IssueCommentSerializer(BaseSerializer):

    class Meta:
        model = IssueComment
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

    def to_representation(self, instance):
        # Usa UserLightSerializer para la representación en las respuestas
        representation = super().to_representation(instance)
        representation["created_by"] = UserLightSerializer(
            instance.created_by).data
        return representation
