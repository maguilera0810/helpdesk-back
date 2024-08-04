from rest_framework import status
from rest_framework.response import Response

from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from api.management.services.task_service import TaskService
from apps.management.serializers import TaskSerializer
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
        """
        Method: POST
        """
        data = request.data
        user = request.user

        error, task = self.srv_class.create_task(user=user,
                                                 data=data)
        if user:
            serializer = self.serial_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_code": error})

    @schema(action="update")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # @schema(action="partial_update")
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)

    @schema(action="destroy")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
