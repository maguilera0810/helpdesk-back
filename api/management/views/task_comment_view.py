# .\api\management\views\task_comment_view.py
from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from api.management.serializers.task_comment_serializer import \
    TaskCommentSerializer
from api.management.services.task_comment_service import TaskCommentService
from resources.decorators.swagger_decorators import custom_swagger_schema


class TaskCommentView(BaseCRUDView, IsAuthenticatedView):
    """TaskComment API View"""

    srv_class: type[TaskCommentService] = TaskCommentService
    serial_class: type[TaskCommentSerializer] = TaskCommentSerializer
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
