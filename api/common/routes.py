# .\api\common\routes.py
from django.urls import path
from api.core.routes import get_crud_route
from api.common.views.skill_view import SkillView

urlpatterns = [
    # PLAN
    *get_crud_route("skill", SkillView),
]
