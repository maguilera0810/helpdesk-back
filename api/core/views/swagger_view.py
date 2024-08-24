from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

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
    permission_classes=(AllowAny,),
)
