# .\apps\authentication\dtos.py
from dataclasses import dataclass
from datetime import datetime


@dataclass
class AuthDTO:
    """
    email: str
    pasword: str
    """
    email: str
    password: str
