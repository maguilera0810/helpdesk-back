# .\api\management\routes.py
from api.core.routes import get_crud_route
from api.management.views.issue_view import IssueView
from api.management.views.issue_file_view import IssueFileView
from api.management.views.plan_view import PlanView
from api.management.views.task_view import TaskView

urlpatterns = [
    # PLAN
    *get_crud_route("plan", PlanView),
    # TASK
    *get_crud_route("task", TaskView),
    # ISSUE
    *get_crud_route("issue", IssueView),
    # ISSUE_FILE
    *get_crud_route("issue-file", IssueFileView, True),
]
