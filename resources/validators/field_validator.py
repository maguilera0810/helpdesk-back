# .\resources\validators\field_validator.py
import re

from resources.enums import ValidatorMsgEnum


class FieldValidator:

    @classmethod
    def validate_data(cls, *args, **kwargs):
        errors = []
        for k, v in kwargs.items():
            print(k, v)
            if validator := getattr(FieldValidator, f"validate_{k}", None):
                is_valid, error = validator(v)
                if not is_valid:
                    errors.append(error)
        return not bool(errors), errors

    @classmethod
    def validate_email(cls, email: str):
        pattern = re.compile( r'^[\w\.\+\-]+@[a-zA-Z\d\-]+(\.[a-zA-Z\d\-]+)*\.[a-zA-Z]{2,}$')
        if pattern.match(email):
            return True, ValidatorMsgEnum.EMAIL_OK
        return False, ValidatorMsgEnum.EMAIL_ERROR

    @classmethod
    def validate_password(cls, password: str):
        if len(password) < 8:
            return False, ValidatorMsgEnum.PASSWORD_LENGTH_ERROR
        if not re.search(r'[A-Z]', password):
            return False, ValidatorMsgEnum.PASSWORD_UPPERCASE_ERROR
        if not re.search(r'[a-z]', password):
            return False, ValidatorMsgEnum.PASSWORD_LOWERCASE_ERROR
        if not re.search(r'\d', password):
            return False, ValidatorMsgEnum.PASSWORD_NUMBER_ERROR
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{};\\|,.<>\/?]', password):
            return False, ValidatorMsgEnum.PASSWORD_SPECIAL_CHAR_ERROR
        return True, ValidatorMsgEnum.PASSWORD_OK

    @classmethod
    def validate_phone(cls, phone: str):
        pattern = re.compile(r'^\+?\d{9,15}$')
        if pattern.match(phone):
            return True, ValidatorMsgEnum.PHONE_OK
        return False, ValidatorMsgEnum.PHONE_ERROR
