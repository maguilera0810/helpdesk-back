# .\api\v1\authentication\routes.py
from django.urls import path
from v1.authentication.views.auth_view import AuthView

urlpatterns = [
    path("login/", AuthView.as_view({"post": "login"}), name="v1_login"),
]
