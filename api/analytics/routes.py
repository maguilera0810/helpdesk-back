# .\api\common\routes.py
from django.urls import path

from api.analytics.views.kpi_view import KPIView

urlpatterns = [
    path("kpi/", KPIView.as_view({"get": "get_kpis"})),
]
