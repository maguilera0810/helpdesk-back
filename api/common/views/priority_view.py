# .\api\common\views\priority_view.py
from api.common.serializers.priority_serializer import PrioritySerializer
from api.common.services.priority_service import PriorityService
from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from resources.decorators.swagger_decorators import custom_swagger_schema


class PriorityView(BaseCRUDView, IsAuthenticatedView):

    srv_class: type[PriorityService] = PriorityService
    serial_class: type[PrioritySerializer] = PrioritySerializer
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
