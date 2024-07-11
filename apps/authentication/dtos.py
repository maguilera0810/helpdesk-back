# .\apps\authentication\dtos.py
from dataclasses import dataclass, field
from typing import Optional


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
