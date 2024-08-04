from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Helpdesk API",
        default_version="v1",
        description="API documentation for Helpdesk",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="maguilera0810@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    # TODO CAMBIAR PERMISOS A ADMIN
    permission_classes=(permissions.AllowAny,),
)
