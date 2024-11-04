# .\api\analytics\routes.py
from django.urls import path

from api.analytics.views.data_analytics_view import DataAnalyticView

urlpatterns = [
    path("data/", DataAnalyticView.as_view({"get": "get_all"})),
]
