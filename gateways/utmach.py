import requests
from apps.authentication.dtos import AuthDTO


class UTMACH:

    @staticmethod
    def check_user(auth: AuthDTO):
        return 200, {
            'name': 'Mauricio Aguilera',
            'email': 'maguilera0810@gmail.com',
            'tfno': '0998877665'
        }
