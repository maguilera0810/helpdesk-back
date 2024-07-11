# .\api\authentication\routes.py
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from api.authentication.views.auth_view import (AuthDetailView, AuthView,
                                                CustomTokenObtainPairView)

urlpatterns = [
    path(
        "user-info/", AuthDetailView.as_view({"get": "get_user_info"}), name="user_info"),
    path("register/", AuthView.as_view({"post": "register"}), name="register"),
    path("token/", CustomTokenObtainPairView.as_view({"post": "obtain_pair"}), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]


"""
obtain-pair
{"username": "mauricio@familify.com", "password": "123456"}
refresh
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6NDgxMDg5Mzc2MiwiaWF0IjoxNjU3MjkzNzYyLCJqdGkiOiI2MTYwNmI2MWNjZjY0M2YzYTJhZWRhMGM1NzNjYTkwNCIsInVzZXJfaWQiOjEwMzc0MjR9.SMa4m2lvoEEQmihh0PmpFSTVZB9oz2LI4NnBdkKRzdk"
}
verify
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYyNzI1MDAyLCJpYXQiOjE2NjI0NjU4MDIsImp0aSI6IjQ4YzNjOWU0MDQyMDQ1OWZiNzFhNGNhNjgwNGMzM2YwIiwidXNlcl9pZCI6ODM4Mjc0fQ.7AQHt6H4Mgq2PQLpgQIgUUOfUfWK66hzDHu5WkNvcww"
}
"""
