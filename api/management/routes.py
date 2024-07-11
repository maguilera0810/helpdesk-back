# .\api\management\routes.py
from django.urls import path
from api.core.routes import METHODS, METHODS_ID
from api.management.views.plan_view import PlanView

urlpatterns = [
    # PLAN
    path("plan/",
         PlanView.as_view({**METHODS}), name="plan"),
    path("plan/<int:id>/",
         PlanView.as_view({**METHODS_ID}), name="plan_id"),
]
