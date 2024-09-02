# .\resources\utils\decode_util.py
import base64
import string
from contextlib import suppress
from secrets import choice
from typing import Optional
from uuid import uuid4

from django.utils.text import slugify


class DecodeUtil:

    @staticmethod
    def base64_to_text(text: str) -> str:
        base64_bytes = text.encode("ascii")
        message_bytes = base64.b64decode(base64_bytes)
        return message_bytes.decode("ascii")

    @staticmethod
    def text_to_base64(text: str) -> str:
        base64_bytes = text.encode("ascii")
        message_bytes = base64.b64encode(base64_bytes)
        return message_bytes.decode("ascii")

    @staticmethod
    def generate_random_code(length: int = 50, upper: bool = False) -> str:
        characters = string.digits
        characters += string.ascii_uppercase if upper else string.ascii_lowercase
        return "".join(choice(characters) for _ in range(length))

    @staticmethod
    def generate_secure_token(length: int = 50, has_punctuation: bool = False) -> str:
        characters = string.ascii_letters + string.digits
        if has_punctuation:
            characters += string.punctuation
        return "".join(choice(characters) for _ in range(length))

    @staticmethod
    def generate_default_string(prefix: str) -> str:
        prefix_slug = slugify(prefix)
        uuid_code = str(uuid4()).replace("-", "")
        return f"{prefix_slug}_{uuid_code}"

    @staticmethod
    def generate_uuid4() -> str:
        return str(uuid4())

    @staticmethod
    def parse_int(text: str) -> Optional[int]:
        with suppress(Exception):
            return int(text)

    @staticmethod
    def text_to_hex(text: str) -> str:
        return text.encode().hex()

    @staticmethod
    def hex_to_text(hex_str: str) -> str:
        return bytes.fromhex(hex_str).decode()
