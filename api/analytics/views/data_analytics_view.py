# .\api\management\views\issue_view.py
from rest_framework import status
from rest_framework.response import Response

from api.analytics.services.data_analytics_service import DataAnalyticService
from api.core.views.base_permission_view import IsAuthenticatedView
from resources.enums import PeriodEnum
from resources.utils.filter_util import FilterUtil


class DataAnalyticView(IsAuthenticatedView):

    def get_all(self, request):
        data = FilterUtil.parser_queryparams(request.GET)
        period = data.get("period", PeriodEnum.today)
        srv = DataAnalyticService(period=period)
        data = srv.get_all()
        return Response(data, status=status.HTTP_200_OK)
