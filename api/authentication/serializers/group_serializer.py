# .\api\authentication\serializers\auth_serializers.py
from django.contrib.auth.models import Group

from api.core.serializers.base_serializer import BaseSerializer


class GroupSerializer(BaseSerializer):
    class Meta:
        model = Group
        fields = "__all__"
