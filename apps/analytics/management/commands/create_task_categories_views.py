# .\apps\analytics\management\commands\create_task_categories_views.py
from django.core.management.base import BaseCommand

from resources.utils.cursor_util import CursorUtil as Cursor

period_filters = {
    "today": " mt.created_at :: date = CURRENT_DATE ",
    "yesterday": " mt.created_at :: date = CURRENT_DATE - INTERVAL '1 day' ",
    "2_days_ago": " mt.created_at :: date = CURRENT_DATE - INTERVAL '2 days' ",
    "last_7_days": " mt.created_at >= CURRENT_DATE - INTERVAL '7 days' ",
    "last_14_days": " mt.created_at >= CURRENT_DATE - INTERVAL '14 days' ",
    "last_month": " mt.created_at >= date_trunc('month', CURRENT_DATE) ",
    "last_3_months": " mt.created_at >= CURRENT_DATE - INTERVAL '3 months' ",
    "current_year": " mt.created_at >= date_trunc('year', CURRENT_DATE) ",
    "last_5_years": " mt.created_at >= CURRENT_DATE - INTERVAL '5 years' ",
}
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
