# .\resources\utils\translation_util.py
from contextlib import suppress

from django.utils.translation import activate, gettext


class TranslationUtil:
    @classmethod
    def set_lang(cls, lang: str) -> None:
        """Ret current lang"""
        activate(lang)

    @classmethod
    def get_translation(cls, string: str, lang: str = "") -> str:
        """Returns a traslated string"""
        if lang:
            cls.set_lang(lang=lang)
        translated = ""
        with suppress(Exception):
            translated = gettext(string)
        return "" if translated == string else translated
