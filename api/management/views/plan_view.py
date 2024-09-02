# .\api\management\views\plan_view.py
from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from api.management.services.plan_service import PlanService
from apps.management.serializers import PlanSerializer
from resources.decorators.swagger_decorators import custom_swagger_schema


class PlanView(BaseCRUDView, IsAuthenticatedView):
    """Plan API View"""

    srv_class: type[PlanService] = PlanService
    serial_class: type[PlanSerializer] = PlanSerializer
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

    # @schema(action="partial_update")
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)

    @schema(action="destroy")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
