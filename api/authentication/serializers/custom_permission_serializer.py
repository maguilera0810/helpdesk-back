# .\api\authentication\serializers\custom_permission_serializer.py
from api.core.serializers.base_serializer import BaseSerializer
from apps.authentication.models import Permission


class PermissionSerializer(BaseSerializer):

    class Meta:
        model = Permission
        fields = "__all__"
