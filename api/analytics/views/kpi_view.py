# .\api\management\views\issue_view.py
from rest_framework import status
from rest_framework.response import Response

from api.analytics.services.kpi_service import KPIService
from api.core.views.base_permission_view import IsAuthenticatedView


class KPIView(IsAuthenticatedView):
    """KPI API View"""

    def get_kpis(self, request):
        data = request.GET
        period = data.get("period", "today")
        srv = KPIService(period=period)
        data = srv.get_kpis()
        return Response(data, status=status.HTTP_200_OK)
