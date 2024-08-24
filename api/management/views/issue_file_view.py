from rest_framework import status
from rest_framework.response import Response

from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from api.management.serializers.issue_file_serializer import \
    IssueFileSerializer
from api.management.services.issue_file_service import IssueFileService
from resources.decorators.swagger_decorators import custom_swagger_schema


class IssueFileView(BaseCRUDView, IsAuthenticatedView):
    """IssueFile API View"""

    srv_class: type[IssueFileService] = IssueFileService
    serial_class: type[IssueFileSerializer] = IssueFileSerializer
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

    @schema(action="update_files")
    def update_files(self, request, *args, **kwargs):
        return super().update_files(request, *args, **kwargs)
