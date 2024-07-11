from api.management.services.plan_service import PlanService
from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from apps.management.serializers import PlanSerializer


class PlanView(BaseCRUDView, IsAuthenticatedView):
    """Plan API View"""

    srv_class: type[PlanService] = PlanService
    serial_class: type[PlanSerializer] = PlanSerializer
