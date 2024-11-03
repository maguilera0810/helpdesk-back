# .\api\routes.py
from django.urls import include, path

urlpatterns = [
    path("analytics/", include("api.analytics.routes")),
    path("auth/", include("api.authentication.routes")),
    path("common/", include("api.common.routes")),
    path("management/", include("api.management.routes")),
]
