# .\resources\utils\cursor_util.py
from django.db import connections

from resources.enums import PeriodEnum


class CursorUtil:

    @classmethod
    def execute(cls, query: str, params: tuple | list = None, try_fetch: bool = True, db: str = "default"):
        cursor = connections[db].cursor()
        try:
            cursor.execute(query, params)
            if try_fetch:
                return cursor.fetchall()
        finally:
            cursor.close()

    @classmethod
    def get_issue_status(cls, period: PeriodEnum):
        query = """
        select
            ispv.status,
            ispv.count
        from
            issue_status_periods_view ispv
        where
            ispv."period" = %s;
        """
        return cls.execute(query=query,
                           params=[period])

    @classmethod
    def get_task_status(cls, period: PeriodEnum):
        query = """
        select
            tspv.status,
            tspv.count
        from
            task_status_periods_view tspv
        where
            tspv."period" = %s;
        """
        return cls.execute(query=query,
                           params=[period])

    @classmethod
    def get_task_categories(cls, period: PeriodEnum):
        query = """
        select
            tcv.category_id,
            tcv.count 
        from
            task_categories_view tcv
        where
            tcv."period" = %s;
        """
        return cls.execute(query=query,
                           params=[period])

    @classmethod
    def get_issue_categories(cls, period: PeriodEnum):
        query = """
        select
            icv.category_id,
            icv.count
        from
            issue_categories_view icv
        where
            icv."period" = %s;
        """
        return cls.execute(query=query,
                           params=[period])
