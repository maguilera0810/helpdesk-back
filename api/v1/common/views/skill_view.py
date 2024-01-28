from rest_framework import status
from rest_framework.response import Response

from api.base.views import IsAuthenticatedView
from apps.common.models import Skill
from apps.common.serializers import SkillSerializer


class SkillView(IsAuthenticatedView):

    def list(self, request):
        filters = request.GET.dict()
        skills = Skill.objects.filter(**filters).order_by("id")
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, id):
        try:
            skill = Skill.objects.get(id=id)
        except Skill.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        serializer = SkillSerializer(skill, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        serializer = SkillSerializer(data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, id):
        try:
            skill = Skill.objects.get(id=id)
        except Skill.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = SkillSerializer(skill, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, id):
        try:
            skill = Skill.objects.get(id=id)
        except Skill.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        skill.delete()
        return Response({}, status=status.HTTP_200_OK)
