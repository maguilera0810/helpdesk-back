# .\api\authentication\views\permission_view.py
from api.authentication.serializers.custom_permission_serializer import \
    CustomPermissionSerializer
from api.authentication.services.custom_permission_service import \
    CustomPermissionService
from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAdminView
from resources.decorators.swagger_decorators import custom_swagger_schema


class CustomPermissionView(BaseCRUDView, IsAdminView):
    """Permission API View"""

    srv_class: type[CustomPermissionService] = CustomPermissionService
    serial_class: type[CustomPermissionSerializer] = CustomPermissionSerializer
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
