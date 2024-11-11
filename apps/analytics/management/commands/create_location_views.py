# .\apps\analytics\management\commands\create_status_views.py
from django.core.management.base import BaseCommand

from resources.enums import PeriodEnum
from resources.utils.cursor_util import CursorUtil as Cursor

alias_filter = {
    "t": "<<main_filters>>",
    "inner_t": "<<inner_filters>>",
}
period_filters = {
    PeriodEnum.today: " <<alias>>.created_at :: date = CURRENT_DATE ",
    PeriodEnum.yesterday: " <<alias>>.created_at :: date = CURRENT_DATE - INTERVAL '1 day' ",
    PeriodEnum.last_7_days: " <<alias>>.created_at >= CURRENT_DATE - INTERVAL '7 days' ",
    PeriodEnum.last_30_days: " <<alias>>.created_at >= CURRENT_DATE - INTERVAL '30 days' ",
    PeriodEnum.last_year: " <<alias>>.created_at >= CURRENT_DATE - INTERVAL '1 year' ",
    PeriodEnum.current_month: " <<alias>>.created_at >= date_trunc('month', CURRENT_DATE) ",
    PeriodEnum.current_year: " <<alias>>.created_at >= date_trunc('year', CURRENT_DATE) ",
    PeriodEnum.all_time: " true ",
}

join_clause = " UNION ALL "
task_base_query = "create or replace view location_task_preriods_view as <<content>>;"
task_content_query = """
select loc.id as location_id, '<<period>>' as "period", coalesce(COUNT(t.id), 0) as task_count,
coalesce((select jsonb_object_agg(sub_cat.id, sub_count.count) from common_category as sub_cat
join ( select tc.category_id, COUNT(tc.category_id) as count
from management_task as inner_t join management_task_categories as tc on inner_t.id = tc.task_id
where inner_t.location_id = loc.id and <<inner_filters>> group by tc.category_id having count(tc.category_id) > 0
) as sub_count on sub_cat.id = sub_count.category_id ), '{}' :: jsonb ) as category_counts
from common_location as loc left join management_task as t on t.location_id = loc.id where <<main_filters>> group by loc.id 
"""

issue_base_query = "create or replace view location_issue_preriods_view as <<content>>;"
issue_content_query = """
select loc.id as location_id, '<<period>>' as "period", coalesce(COUNT(t.id), 0) as issue_count,
coalesce((select jsonb_object_agg(sub_cat.id, sub_count.count) from common_category as sub_cat
join ( select tc.category_id, COUNT(tc.category_id) as count
from management_issue as inner_t join management_issue_categories as tc on inner_t.id = tc.issue_id
where inner_t.location_id = loc.id and <<inner_filters>> group by tc.category_id having count(tc.category_id) > 0
) as sub_count on sub_cat.id = sub_count.category_id ), '{}' :: jsonb ) as category_counts
from common_location as loc left join management_issue as t on t.location_id = loc.id where <<main_filters>> group by loc.id
"""


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.create_location_task_view()
        self.create_location_issue_view()

    def create_location_task_view(self):
        def fn(period: str, filters: str):
            res = task_content_query.replace("<<period>>", period)
            for alias, filter_key in alias_filter.items():
                clean_filters = filters.replace("<<alias>>", alias)
                res = res.replace(filter_key, clean_filters)
            return res
        contents = [fn(*i) for i in period_filters.items()]
        content = join_clause.join(contents)
        final_query = task_base_query.replace("<<content>>",
                                              content)
        print()
        print(final_query)
        print()
        Cursor.execute(query=final_query,
                       try_fetch=False)

    def create_location_issue_view(self):
        def fn(period: str, filters: str):
            res = issue_content_query.replace("<<period>>", period)
            for alias, filter_key in alias_filter.items():
                clean_filters = filters.replace("<<alias>>", alias)
                res = res.replace(filter_key, clean_filters)
            return res
        contents = [fn(*i) for i in period_filters.items()]
        content = join_clause.join(contents)
        final_query = issue_base_query.replace("<<content>>",
                                               content)
        print()
        print(final_query)
        print()
        Cursor.execute(query=final_query,
                       try_fetch=False)
