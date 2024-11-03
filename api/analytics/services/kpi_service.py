from collections import defaultdict

from resources.enums import IssueStatusEnum, PeriodEnum, TaskStatusEnum
from resources.utils.cursor_util import CursorUtil as Cursor


class KPIService:
    cursor = Cursor

    def __init__(self, period: PeriodEnum):
        self.period = period
        self.status_taks = defaultdict(int)
        self.status_issues = defaultdict(int)

    def get_kpis(self):
        return {
            "status_taks": self.get_status_task(),
            "status_issues": self.get_status_issues(),
        }

    def get_status_tasks(self):
        for i in TaskStatusEnum.values:
            self.status_taks[i]
        rows = Cursor.get_task_status(period=self.period)
        for status, value in rows:
            self.status_taks[status] = value
        return self.status_taks

    def get_status_issues(self):
        for i in IssueStatusEnum.values:
            self.status_issues[i]
        rows = Cursor.get_issue_status(period=self.period)
        for status, value in rows:
            self.status_issues[status] = value
        return self.status_issues
