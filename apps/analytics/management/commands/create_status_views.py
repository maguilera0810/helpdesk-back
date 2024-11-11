# .\apps\analytics\management\commands\create_status_views.py
from django.core.management.base import BaseCommand

from resources.enums import PeriodEnum
from resources.utils.cursor_util import CursorUtil as Cursor

period_filters = {k: v.replace("<<alias>>.", "").replace("created_at", "updated_at")
                  for k, v in PeriodEnum.choices}
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
