# .\api\management\routes.py
from django.urls import path

from api.core.routes import get_crud_route
from api.management.views.plan_view import PlanView
from api.management.views.task_view import TaskView

urlpatterns = [
    # PLAN
    *get_crud_route("plan", PlanView),
    # TASK
    *get_crud_route("task", TaskView),
]
