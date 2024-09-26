# .\api\management\services\task_service.py
from collections import defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

from django.conf import settings
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Q
from django.utils import timezone

from api.core.services.base_crud_service import BaseCRUDService
from api.management.serializers.task_serializer import TaskSerializer
from apps.management.models import Task

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"  # Formato ISO 8601
LOCAL_TZ = ZoneInfo(settings.TIME_ZONE)


class TaskService(BaseCRUDService):
    model = Task

    @transaction.atomic
    def create(self, data: dict):
        """
        + title
        + description
        - code
        + type
        + status
        + priority
        + created_by: por el token de usuario
        + responsible
        + team
        + plan
        + scheduled
        // date_execution
        // interval
        - created_at
        - updated_at
        """
        serializer = TaskSerializer(data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors

    @transaction.atomic
    def update(self, data: dict, task_id: int, task: Task):
        task = task or self.get_one(task_id)
        serializer = TaskSerializer(instance=task, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors

    @classmethod
    def retrieve_schedule(cls, responsible_id: int, team: list[int],
                          start_at: datetime, end_at: datetime,
                          curr_task_id: int = None):

        if not isinstance(start_at, datetime):
            start_at = datetime.strptime(start_at, DATE_FORMAT)
        if not isinstance(end_at, datetime):
            end_at = datetime.strptime(end_at, DATE_FORMAT)

        start_at = timezone.make_aware(start_at, timezone=timezone.utc)
        end_at = timezone.make_aware(end_at, timezone=timezone.utc)

        # start_at = start_at.astimezone(LOCAL_TZ)
        # end_at = end_at.astimezone(LOCAL_TZ)

        start_date = start_at.date()
        end_date = end_at.date()

        responsible_tasks = cls.__query_tasks(user_id=responsible_id,
                                              start_date=start_date,
                                              end_date=end_date)
        has_collision = False
        for task in responsible_tasks:
            collition = cls.__check_task_collision(curr_task_id=curr_task_id,
                                                   task=task,
                                                   start_at=start_at,
                                                   end_at=end_at)
            has_collision = has_collision or collition
        user_tasks = [{"user_id": responsible_id,
                      "tasks": responsible_tasks}]

        team = [t for t in team if t != responsible_id]
        for user_id in team:
            team_tasks = cls.__query_tasks(user_id=user_id,
                                           start_date=start_date,
                                           end_date=end_date)
            for task in team_tasks:
                collition = cls.__check_task_collision(curr_task_id=curr_task_id,
                                                       task=task,
                                                       start_at=start_at,
                                                       end_at=end_at)
                has_collision = has_collision or collition
            user_tasks.append({"user_id": user_id,
                              "tasks": team_tasks})
        return {
            "has_collision": has_collision,
            "user_tasks": user_tasks
        }

    @classmethod
    def __query_tasks(cls, user_id, start_date, end_date):
        return Task.objects.filter(Q(responsible__id=user_id) | Q(team__id=user_id))\
            .exclude(Q(start_at=None) | Q(end_at=None))\
            .filter(Q(start_at__date__gte=start_date, start_at__date__lte=end_date) |
                    Q(end_at__date__gte=start_date, end_at__date__lte=end_date))\
            .values("id", "title", "start_at", "end_at").order_by("start_at").distinct()

    @classmethod
    def __check_task_collision(cls, curr_task_id: int, task: dict, start_at: datetime, end_at: datetime):
        task["has_collision"] = (task["id"] != curr_task_id and
                                 task["start_at"] <= end_at and
                                 task["end_at"] <= start_at)
