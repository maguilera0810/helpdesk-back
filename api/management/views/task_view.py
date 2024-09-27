# .\api\management\views\task_view.py
from rest_framework import status
from rest_framework.response import Response

from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from api.management.serializers.task_serializer import TaskSerializer
from api.management.services.task_service import TaskService
from resources.decorators.swagger_decorators import custom_swagger_schema


class TaskView(BaseCRUDView, IsAuthenticatedView):
    """Task API View"""

    srv_class: type[TaskService] = TaskService
    serial_class: type[TaskSerializer] = TaskSerializer
    schema = custom_swagger_schema(serial_class)

    @schema(action="list")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @schema(action="retrieve")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @schema(action="create")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @schema(action="update")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @schema(action="destroy")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @schema(action="retrieve_schedule",
            description="Create a Task from a Issue",
            responses={status.HTTP_200_OK: "OK",
                       status.HTTP_201_CREATED: "CREATED",
                       status.HTTP_400_BAD_REQUEST: "BAD_REQUEST"})
    def retrieve_schedule(self, request):
        data = request.data
        responsible_id = data["responsible_id"]
        team = data["team"]
        start_at = data["start_at"]
        end_at = data["end_at"]
        curr_task_id = data.get("curr_task_id")
        schedules = self.srv_class.retrieve_schedule(responsible_id=responsible_id,
                                                     team=team,
                                                     start_at=start_at,
                                                     end_at=end_at,
                                                     curr_task_id=curr_task_id)
        return Response(schedules, status=status.HTTP_200_OK)
