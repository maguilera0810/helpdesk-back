from rest_framework import status
from rest_framework.response import Response

from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from api.management.serializers.issue_serializer import IssueSerializer
from api.management.serializers.task_serializer import TaskSerializer
from api.management.services.issue_service import IssueService
from resources.decorators.swagger_decorators import custom_swagger_schema


class IssueView(BaseCRUDView, IsAuthenticatedView):
    """Issue API View"""

    srv_class: type[IssueService] = IssueService
    serial_class: type[IssueSerializer] = IssueSerializer
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

    @schema(action="create_task",
            description="Create a Task from a Issue",
            responses={status.HTTP_200_OK: TaskSerializer(),
                       status.HTTP_201_CREATED: "CREATED",
                       status.HTTP_400_BAD_REQUEST: "BAD_REQUEST", })
    def create_task(self, request, id: int):
        srv = self.srv_class(user=request.user)
        errors, data = srv.create_task(id=id,
                                       request=request)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data["id"], status=status.HTTP_201_CREATED)
