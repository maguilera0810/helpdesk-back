# .\api\management\views\task_status_view.py
from rest_framework import status
from rest_framework.response import Response

from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from api.management.serializers.task_status_serializer import \
    TaskStatusSerializer
from api.management.services.task_status_service import TaskStatusService
from resources.decorators.swagger_decorators import custom_swagger_schema


class TaskStatusView(BaseCRUDView, IsAuthenticatedView):
    """TaskStatus API View"""

    srv_class: type[TaskStatusService] = TaskStatusService
    serial_class: type[TaskStatusSerializer] = TaskStatusSerializer
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
