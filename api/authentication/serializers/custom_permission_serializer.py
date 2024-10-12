# .\api\authentication\serializers\permission_serializer.py
from api.core.serializers.base_serializer import BaseSerializer
from apps.authentication.models import CustomPermission


class CustomPermissionSerializer(BaseSerializer):

    class Meta:
        model = CustomPermission
        fields = "__all__"
