# .\api\analytics\services\data_analytics_service.py
from collections import defaultdict

from apps.common.models import Category
from resources.enums import IssueStatusEnum, PeriodEnum, TaskStatusEnum
from resources.utils.cursor_util import CursorUtil as Cursor


class DataAnalyticService:
    cursor = Cursor

    def __init__(self, period: PeriodEnum):
        self.period = period
        self.task_status = defaultdict(int)
        self.issues_status = defaultdict(int)

    def __set_categories(self, category_ids):
        cats = (Category.objects.filter(id__in=category_ids)
                .values("id", "title").all())
        return {c["id"]: c for c in cats}

    def get_all(self):
        return {
            **self.get_category_data(),
            **self.get_status(),
        }

    def get_category_data(self):
        task_rows = Cursor.get_task_categories(period=self.period)
        issue_rows = Cursor.get_issue_categories(period=self.period)
        category_ids = {*(t[0] for t in task_rows),
                        *(i[0] for i in issue_rows)}
        categories = self.__set_categories(category_ids)
        return {
            "task_categories": self.get_category_list(rows=task_rows,
                                                      categories=categories),
            "issue_categories": self.get_category_list(rows=issue_rows,
                                                       categories=categories),
        }

    def get_category_list(self, rows, categories: dict):
        res = []
        for category_id, value in rows:
            if category := categories.get(category_id):
                res.append({**category,
                            "value": value})
            elif category_id == -1:
                res.append({
                    "id": category_id,
                    "title": "N/A",
                    "value": value})
        return res

    def get_status(self):
        return {
            "task_status": self.get_task_status(),
            "issue_status": self.get_issue_status(),
        }

    def get_task_status(self):
        for i in TaskStatusEnum.values:
            self.task_status[i]
        rows = Cursor.get_task_status(period=self.period)
        for status, value in rows:
            self.task_status[status] = value
        return self.task_status

    def get_issue_status(self):
        for i in IssueStatusEnum.values:
            self.issues_status[i]
        rows = Cursor.get_issue_status(period=self.period)
        for status, value in rows:
            self.issues_status[status] = value
        return self.issues_status
