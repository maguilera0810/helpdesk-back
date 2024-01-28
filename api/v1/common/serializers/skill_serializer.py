from apps.common.models import Skill
from rest_framework.serializers import ModelSerializer


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = (
            "id",
            "name",
            "description",
        )


class SkillListSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = (
            "id",
            "name",
        )
