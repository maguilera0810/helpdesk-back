# .\api\authentication\serializers\role_serializer.py
from api.core.serializers.base_serializer import BaseSerializer
from apps.authentication.models import Role


class RoleSerializer(BaseSerializer):
    class Meta:
        model = Role
        fields = "__all__"
