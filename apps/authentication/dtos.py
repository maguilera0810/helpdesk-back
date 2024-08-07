# .\apps\authentication\dtos.py
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProfileDTO:
    """
    Data transfer object for profile details.
    """
    id: Optional[int] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    document_type: Optional[str] = None
    document: Optional[str] = None
    is_available: Optional[bool] = None
    user: Optional[int] = None


@dataclass
class UserDTO:
    """
    Data transfer object for user details.
    """
    id: Optional[int] = None
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_superuser: Optional[bool] = None
    is_staff: Optional[bool] = None
    is_active: Optional[bool] = None
    date_joined: Optional[str] = None
    last_login: Optional[str] = None
    groups: Optional[list] = field(default_factory=list)
    user_permissions: Optional[list] = field(default_factory=list)
    profile: Optional[ProfileDTO] = None


@dataclass
class AuthDTO:
    """
    Data transfer object for authentication details.
    """
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    document_type: Optional[str] = None
    document: Optional[str] = None
    is_staff: Optional[bool] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_available: Optional[bool] = None


def map_user_data(data) -> UserDTO:
    """
        {
            'id': 2,
            'email': 'mauricio+0001@gmail.com',
            'first_name': 'Mauricio 0001',
            'last_name': 'Aguilera',
            'username': 'mauricio+0001@gmail.com',
            'last_login': '2024-08-04T20:26:23.226225Z',
            'date_joined': '2024-07-14T18:34:04.175020Z',
            'groups': [],
            'user_permissions': [],
            'is_superuser': True,
            'is_staff': True,
            'is_active': True,
            'profile': {
                'id': 2,
                'phone': '1234567890',
                'address': '',
                'document_type': 'dni',
                'document': '0000000001',
                'is_available': True,
                'user': 2
            },
        }

    """
    profile_data = data.pop("profile", None)
    if profile_data:
        profile = ProfileDTO(**profile_data)
    else:
        profile = None
    user = UserDTO(profile=profile, **data)
    return user
