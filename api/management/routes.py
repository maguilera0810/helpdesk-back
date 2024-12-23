# .\api\management\routes.py
from django.urls import path

from api.core.routes import get_crud_route
from api.management.views.issue_comment_view import IssueCommentView
from api.management.views.issue_file_view import IssueFileView
from api.management.views.issue_view import IssueView
from api.management.views.plan_view import PlanView
from api.management.views.task_comment_view import TaskCommentView
from api.management.views.task_view import TaskView

urlpatterns = [
    path("task/schedule/", TaskView.as_view({"post": "retrieve_schedule"})),
    path("task/tracking/", TaskView.as_view({"post": "tracking_tasks"})),
    path("issue/<int:id>/create-task/",
         IssueView.as_view({"post": "create_task"})),
    *get_crud_route("plan", PlanView),
    *get_crud_route("task", TaskView),
    *get_crud_route("task-comment", TaskCommentView),
    *get_crud_route("issue", IssueView),
    *get_crud_route("issue-file", IssueFileView),
    *get_crud_route("issue-comment", IssueCommentView),
]
