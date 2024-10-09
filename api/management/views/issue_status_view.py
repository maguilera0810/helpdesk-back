# .\api\management\views\issue_status_view.py
from rest_framework import status
from rest_framework.response import Response

from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from api.management.serializers.issue_status_serializer import \
    IssueStatusSerializer
from api.management.serializers.task_serializer import TaskSerializer
from api.management.services.issue_status_service import IssueStatusService
from resources.decorators.swagger_decorators import custom_swagger_schema


class IssueStatusView(BaseCRUDView, IsAuthenticatedView):
    """IssueStatus API View"""

    srv_class: type[IssueStatusService] = IssueStatusService
    serial_class: type[IssueStatusSerializer] = IssueStatusSerializer
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
