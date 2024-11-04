# .\api\management\views\issue_view.py
from rest_framework import status
from rest_framework.response import Response

from api.analytics.services.data_analytics_service import DataAnalyticService
from api.core.views.base_permission_view import IsAuthenticatedView


class DataAnalyticView(IsAuthenticatedView):

    def get_all(self, request):
        data = request.GET
        period = data.get("period", "today")
        srv = DataAnalyticService(period=period)
        data = srv.get_all()
        return Response(data, status=status.HTTP_200_OK)
