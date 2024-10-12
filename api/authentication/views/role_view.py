# .\api\authentication\views\group_view.py
from api.authentication.serializers.role_serializer import RoleSerializer
from api.authentication.services.role_service import RoleService
from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAdminView
from resources.decorators.swagger_decorators import custom_swagger_schema


class RoleView(BaseCRUDView, IsAdminView):
    """Role API View"""

    srv_class: type[RoleService] = RoleService
    serial_class: type[RoleSerializer] = RoleSerializer
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
