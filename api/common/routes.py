# .\api\common\routes.py
from api.common.views.category_type_view import CategoryTypeView
from api.common.views.category_view import CategoryView
from api.common.views.location_view import LocationView
from api.common.views.priority_view import PriorityView
from api.common.views.skill_view import SkillView
from api.common.views.tag_view import TagView
from api.core.routes import get_crud_route

urlpatterns = [
    *get_crud_route("category", CategoryView),
    *get_crud_route("category-type", CategoryTypeView),
    *get_crud_route("location", LocationView),
    *get_crud_route("priority", PriorityView),
    *get_crud_route("skill", SkillView),
    *get_crud_route("tag", TagView),
]
