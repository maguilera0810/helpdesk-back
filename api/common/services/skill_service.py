from api.core.services.base_crud_service import BaseCRUDService
from apps.common.models import Skill


class SkillService(BaseCRUDService):
    model = Skill
