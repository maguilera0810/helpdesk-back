from django.urls import include, path

urlpatterns = [
    path('authentication/', include('api.v1.authentication.routes')),
    path('common/', include('api.v1.common.routes')),
    path('management/', include('api.v1.management.routes')),
]
