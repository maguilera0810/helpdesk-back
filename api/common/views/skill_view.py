# .\api\common\views\skill_view.py
from api.common.services.skill_service import SkillService
from api.core.views.base_crud_view import BaseCRUDView
from api.core.views.base_permission_view import IsAuthenticatedView
from apps.common.models import Skill
from apps.common.serializers import SkillSerializer


class SkillView(BaseCRUDView, IsAuthenticatedView):
    model = Skill
    serial_class = SkillSerializer
