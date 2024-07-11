# .\apps\authentication\dtos.py
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AuthDTO:
    """
    Data transfer object for authentication details.
    """
    email: str
    password: str
    first_name: str
    last_name: str
    document_type: Optional[str] = None
    document: Optional[str] = None
    phone: Optional[str] = None
