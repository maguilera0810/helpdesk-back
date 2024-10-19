# .\api\authentication\routes.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from api.authentication.views.auth_view import CustomTokenObtainPairView
from api.authentication.views.permission_view import PermissionView
from api.authentication.views.role_view import RoleView
from api.authentication.views.user_view import UserView
from api.core.routes import get_crud_route

urlpatterns = [
    # USER
    path("user/info/",
         UserView.as_view({"get": "get_user_info"})),
    path("user/light/",
         UserView.as_view({"get": "list_light"})),
    # path("user/register/",
    #    AuthApiKeyView.as_view({"post": "create"})), # NO SE USA
    *get_crud_route("user", UserView),

    # ROLE
    *get_crud_route("role", RoleView),
    # CUSTOM PERMISSION
    *get_crud_route("permission", PermissionView),
    # TOKEN
    path("token/", CustomTokenObtainPairView.as_view(
        {"post": "obtain_pair"})),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("token/verify/", TokenVerifyView.as_view()),
]


# urlpatterns = [
#     # ADMIN USER
#     *get_crud_route("admin-user", AuthAdminView),
#     # ROLE
#     *get_crud_route("role", RoleView),
#     # CUSTOM PERMISSION
#     *get_crud_route("permission", PermissionView),
#     # USER
#     path("user/info/",
#          AuthDetailView.as_view({"get": "get_user_info"})),
#     path("user/register/",
#          AuthView.as_view({"post": "create"})),
#     # TOKEN
#     path("token/", CustomTokenObtainPairView.as_view(
#         {"post": "obtain_pair"})),
#     path("token/refresh/", TokenRefreshView.as_view()),
#     path("token/verify/", TokenVerifyView.as_view()),
# ]
