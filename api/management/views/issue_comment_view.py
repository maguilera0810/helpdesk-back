# .\api\management\views\issue_comment_view.py
from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from api.management.serializers.issue_comment_serializer import \
    IssueCommentSerializer
from api.management.services.issue_comment_service import IssueCommentService
from resources.decorators.swagger_decorators import custom_swagger_schema


class IssueCommentView(BaseCRUDView, IsAuthenticatedView):
    """IssueComment API View"""

    srv_class: type[IssueCommentService] = IssueCommentService
    serial_class: type[IssueCommentSerializer] = IssueCommentSerializer
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
