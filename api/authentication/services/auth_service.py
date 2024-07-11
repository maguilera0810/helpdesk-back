# .\api\authentication\services\auth_service.py
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Q

from api.core.services.base_crud_service import BaseCRUDService
from apps.authentication.dtos import AuthDTO
from apps.authentication.models import Profile
from resources.enums import AuthMsgEnum
from resources.validators.field_validator import FieldValidator


class AuthService(BaseCRUDService):
    model = User

    @classmethod
    @transaction.atomic
    def create_user(cls, data: AuthDTO):
        is_valid, errors = FieldValidator.validate_data(email=data.email,
                                                        phone=data.phone,
                                                        password=data.password)
        print(is_valid, errors)
        if not is_valid:
            return errors, None
        if User.objects.filter(Q(email=data.email) |
                               Q(profile__document=data.document)).exists():
            return [AuthMsgEnum.USER_ALREADY_EXIST], None
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
        return [], user

    @classmethod
    @transaction.atomic
    def update_user(cls, id: int, data: AuthDTO):
        is_valid, errors = FieldValidator.validate_data(email=data.email,
                                                        phone=data.phone)
        if not is_valid:
            return errors, None
        user = User.objects.filter(id=id).first()
        if not user:
            return [AuthMsgEnum.USER_DOES_NOT_EXIST], None
        if User.objects.filter(email=data.email).exclude(id=id).exists():
            return [AuthMsgEnum.EMAIL_ALREADY_EXIST], None
        user.email = data.email
        user.first_name = data.first_name
        user.last_name = data.last_name
        user.is_staff = data.is_staff
        user.is_active = data.is_active
        user.is_superuser = data.is_superuser
        user.save()
        profile: Profile = user.profile
        profile.phone = data.phone
        profile.address = data.address
        profile.document_type = data.document_type
        profile.document = data.document
        profile.is_available = data.is_available
        profile.save()
        return [], user

    @classmethod
    @transaction.atomic
    def update_password(cls, id: int, data: AuthDTO):
        is_valid, errors = FieldValidator.validate_password(data.password)
        if not is_valid:
            return errors, None
        if user := User.objects.filter(id=id).first():
            user.set_password(data.password)
            user.save()
            return [], user
        return [AuthMsgEnum.USER_DOES_NOT_EXIST], None

    @classmethod
    @transaction.atomic
    def delete_user(cls, id: int):
        user = User.objects.filter(id=id).first()
        if not user:
            return
        profile = user.profile
        profile.delete()
        user.delete()
        return True
