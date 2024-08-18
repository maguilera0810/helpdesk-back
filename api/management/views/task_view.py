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
        """
        Method: POST

        Request:
            - title (str)
            - description (str)
            - code (str)
            - type (str)
            - status 
            - priority
            - created_by: por el token de usuario
            - responsible
            - team
            - plan
            - scheduled
            - date_execution TODO
            - interval TODO
        """
        data = request.data
        user = request.user

        serializer = self.serial_class(data=data,
                                       partial=True,
                                       context={"request_user": user})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @schema(action="update")
    def update(self, request, id, *args, **kwargs):
        return super().update(request, *args, **kwargs)
        """
        Method: PUT

        Request:
            - title (str)
            - description (str)
            - code (str)
            - type (str)
            - status 
            - priority
            - created_by: por el token de usuario
            - responsible
            - team
            - plan
            - scheduled
            - date_execution TODO
            - interval TODO
        """
        data = request.data
        user = request.user

        if not (task := self.srv_class.get_one(id=id)):
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serial_class(task,
                                       data=data,
                                       partial=True,
                                       context={"request_user": user})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @schema(action="destroy")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
