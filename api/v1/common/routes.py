# .\api\v1\common\routes.py
from django.urls import path

from api.v1.common.views.skill_view import SkillView

urlpatterns = [
    path('skill/', SkillView.as_view({"get": "list",
                                      "post": "create"}), name="v1_skill"),
    path('skill/<int:id>', SkillView.as_view({"get": "retrieve",
                                              "put": "update",
                                              "delete": "destroy"}), name="v1_skill_id"),
]
