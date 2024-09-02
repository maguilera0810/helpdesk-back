# .\api\authentication\serializers\permission_serializer.py
from django.contrib.auth.models import Permission

from api.core.serializers.base_serializer import BaseSerializer


class PermissionSerializer(BaseSerializer):

    class Meta:
        model = Permission
        fields = "__all__"
