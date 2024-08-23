# .\api\management\routes.py
from api.core.routes import get_crud_route
from api.management.views.issue_file_view import IssueFileView
from api.management.views.issue_view import IssueView
from api.management.views.plan_view import PlanView
from api.management.views.task_view import TaskView

urlpatterns = [
    *get_crud_route("plan", PlanView),
    *get_crud_route("task", TaskView),
    *get_crud_route("issue", IssueView),
    *get_crud_route("issue-file", IssueFileView),
]
