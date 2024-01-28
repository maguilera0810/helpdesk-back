from rest_framework.serializers import ModelSerializer

from apps.common.models import Skill


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
