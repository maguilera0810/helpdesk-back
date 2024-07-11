# .\api\authentication\routes.py
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from api.authentication.views.auth_view import (AuthAdminView, AuthDetailView,
                                                AuthView,
                                                CustomTokenObtainPairView)

METHODS = {"get": "list", "post": "create"}
METHODS_ID = {"get": "retrieve", "put": "update", "delete": "destroy"}
METHODS_FILE = {"put": "update_files"}
urlpatterns = [
    # ADMIN USER
    path("admin-user/",
         AuthAdminView.as_view({**METHODS}), name="admin_user"),
    path("admin-user/<int:id>/",
         AuthAdminView.as_view({**METHODS_ID}), name="admin_user_id"),
    # USER
    path("user/info/",
         AuthDetailView.as_view({"get": "get_user_info"}), name="user_info"),
    path("user/register/",
         AuthView.as_view({"post": "create"}), name="register"),
    # TOKEN
    path("token/", CustomTokenObtainPairView.as_view(
        {"post": "obtain_pair"}), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
