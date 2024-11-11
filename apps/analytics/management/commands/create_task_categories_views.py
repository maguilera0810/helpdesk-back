# .\apps\analytics\management\commands\create_task_categories_views.py
from django.core.management.base import BaseCommand

from resources.enums import PeriodEnum
from resources.utils.cursor_util import CursorUtil as Cursor

period_filters = {k: v.replace("<<alias>>", "mt")
                  for k, v in PeriodEnum.choices}

base_query = "CREATE OR REPLACE VIEW task_categories_view AS <<content>>;"
content_query = """
select COALESCE(mtc.category_id, -1)  as category_id, '<<period>>' as period, count(*) as count from management_task mt 
left join management_task_categories mtc on mtc.task_id = mt.id where <<filters>> group by COALESCE(mtc.category_id, -1)
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
