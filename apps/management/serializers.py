# .\apps\management\serializers.py
from rest_framework.serializers import ModelSerializer

from apps.management.models import (Plan, Report, Request, RequestingUnit,
                                    ScheduledTask, Task, TaskHistory)


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class ScheduledTaskSerializer(ModelSerializer):
    class Meta:
        model = ScheduledTask
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class RequestingUnitSerializer(ModelSerializer):
    class Meta:
        model = RequestingUnit
        fields = "__all__"


class RequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"


class TaskHistorySerializer(ModelSerializer):
    class Meta:
        model = TaskHistory
        fields = "__all__"


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
