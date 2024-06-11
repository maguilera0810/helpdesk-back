import requests

from apps.authentication.dtos import AuthDTO


class UTMACH:

    @staticmethod
    def check_user(auth: AuthDTO):
        return 200, {
            "first_name": "Mauricio",
            "last_name": "Aguilera",
            "email": auth.email,
            "phone_number": "0998877665"
        }
