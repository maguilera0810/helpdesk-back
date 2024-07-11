# .\api\authentication\services\auth_service.py
from api.core.services.base_crud_service import BaseCRUDService
from django.contrib.auth.models import User
from apps.authentication.dtos import AuthDTO
from resources.enums import AuthErrorEnum
from django.db import transaction
from apps.authentication.models import Profile
from django.db.models import Q


class AuthService(BaseCRUDService):
    model = User

    @classmethod
    @transaction.atomic
    def create_user(cls, data: AuthDTO):
        if User.objects.filter(Q(email=data.email) |
                               Q(profile__document=data.document)).exists():
            return AuthErrorEnum.user_already_exist, None
        user = User(email=data.email,
                    username=data.email,
                    first_name=data.first_name,
                    last_name=data.last_name)
        user.set_password(data.password)
        user.save()
        profile = Profile(user=user,
                          phone=data.phone,
                          document=data.document,
                          document_type=data.document_type)
        profile.save()
        return None, user
