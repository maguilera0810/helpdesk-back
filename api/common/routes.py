# .\api\common\routes.py
from django.urls import path

from api.common.views.skill_view import SkillView

urlpatterns = [
    # SKILL
    path('skill/', SkillView.as_view({"get": "list",
                                      "post": "create"}), name="skill"),
    path('skill/<int:id>', SkillView.as_view({"get": "retrieve",
                                              "put": "update",
                                              "delete": "destroy"}), name="skill_id"),
]
