# .\resources\utils\decode_util.py
import base64
import hashlib
import string
from contextlib import suppress
from secrets import choice
from typing import Optional
from uuid import uuid4

from django.utils.text import slugify


class DecodeUtil:

    @staticmethod
    def md5(text: str):
        return hashlib.md5(text.encode()).hexdigest()

    @staticmethod
    def sha1(text: str):
        return hashlib.sha1(text.encode()).hexdigest()

    @staticmethod
    def sha224(text: str):
        return hashlib.sha224(text.encode()).hexdigest()

    @staticmethod
    def sha256(text: str):
        return hashlib.sha256(text.encode()).hexdigest()

    @staticmethod
    def sha512(text: str):
        return hashlib.sha512(text.encode()).hexdigest()

    @staticmethod
    def base64_encode(text: str):
        return base64.b64encode(text.encode()).decode()

    @staticmethod
    def base64_decode(encoded_text):
        return base64.b64decode(encoded_text.encode()).decode()

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
