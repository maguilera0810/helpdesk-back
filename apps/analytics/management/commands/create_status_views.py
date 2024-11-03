# .\apps\authentication\management\commands\create_permissions.py
from django.core.management.base import BaseCommand

from resources.utils.cursor_util import CursorUtil as Cursor

period_filters = {
    "today": " updated_at :: date = CURRENT_DATE ",
    "yesterday": " updated_at :: date = CURRENT_DATE - INTERVAL '1 day' ",
    "2_days_ago": " updated_at :: date = CURRENT_DATE - INTERVAL '2 days' ",
    "last_7_days": " updated_at >= CURRENT_DATE - INTERVAL '7 days' ",
    "last_14_days": " updated_at >= CURRENT_DATE - INTERVAL '14 days' ",
    "last_month": " updated_at >= date_trunc('month', CURRENT_DATE) ",
    "last_3_months": " updated_at >= CURRENT_DATE - INTERVAL '3 months' ",
    "current_year": " updated_at >= date_trunc('year', CURRENT_DATE) ",
    "last_5_years": " updated_at >= CURRENT_DATE - INTERVAL '5 years' ",
}
join_clause = " UNION ALL "

task_base_query = "CREATE OR REPLACE VIEW task_status_periods_view AS <<content>>;"
task_content_query = " SELECT status, '<<period>>' AS period, COUNT(*) AS count FROM management_task WHERE <<filters>> GROUP BY status "

issue_base_query = "CREATE OR REPLACE VIEW issue_status_periods_view AS <<content>>;"
issue_content_query = " SELECT status, '<<period>>' AS period, COUNT(*) AS count FROM management_issue WHERE <<filters>> GROUP BY status "


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.create_task_view()
        self.create_issue_view()

    def create_task_view(self):
        def fn(period, filters):
            return task_content_query.replace("<<period>>", period).replace("<<filters>>", filters)
        contents = [fn(*i) for i in period_filters.items()]
        content = join_clause.join(contents)
        final_query = task_base_query.replace("<<content>>",
                                              content)
        print(final_query)
        Cursor.execute(query=final_query,
                       try_fetch=False)

    def create_issue_view(self):
        def fn(period, filters):
            return issue_content_query.replace("<<period>>", period).replace("<<filters>>", filters)
        contents = [fn(*i) for i in period_filters.items()]
        content = join_clause.join(contents)
        final_query = issue_base_query.replace("<<content>>",
                                               content)
        print(final_query)
        Cursor.execute(query=final_query,
                       try_fetch=False)
