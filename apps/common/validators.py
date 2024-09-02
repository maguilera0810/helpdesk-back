# .\apps\common\validators.py
from django.core.validators import RegexValidator


color_validator = RegexValidator(regex=r"^#[0-9A-Fa-f]{6}$",
                                 message="El color debe ser un valor hexadecimal válido",
                                 code="invalid_color")
