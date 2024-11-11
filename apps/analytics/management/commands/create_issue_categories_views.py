# .\apps\analytics\management\commands\create_issue_categories_views.py
from django.core.management.base import BaseCommand

from resources.enums import PeriodEnum
from resources.utils.cursor_util import CursorUtil as Cursor

period_filters = {k: v.replace("<<alias>>", "mi")
                  for k, v in PeriodEnum.choices}


base_query = "CREATE OR REPLACE VIEW issue_categories_view AS <<content>>;"
content_query = """
select COALESCE(mic.category_id, -1) as category_id, '<<period>>' as period, count(*) as count from management_issue mi 
left join management_issue_categories mic on mic.issue_id = mi.id where <<filters>> group by COALESCE(mic.category_id, -1)
"""
join_clause = " UNION ALL "


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.create_view()

    def create_view(self):
        def fn(period, filters):
            return content_query.replace("<<period>>", period).replace("<<filters>>", filters)
        contents = [fn(*i) for i in period_filters.items()]
        content = join_clause.join(contents)
        final_query = base_query.replace("<<content>>",
                                         content)
        print(final_query)
        Cursor.execute(query=final_query,
                       try_fetch=False)
