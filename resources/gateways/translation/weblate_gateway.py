# .\resources\gateways\translation\weblate_gateway.py
import logging
import os
from contextlib import suppress
from pathlib import Path

import requests
from django.conf import settings
from django.core.cache import cache
from django.core.management import call_command

from resources.enums import LanguagesEnum
from resources.gateways.translation import BaseTranslationGateway

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

WEBLATE_URL = settings.WEBLATE_URL
WEBLATE_API_KEY = settings.WEBLATE_API_KEY
WEBLATE_PROJECT = settings.WEBLATE_PROJECT
WEBLATE_COMPONENT = settings.WEBLATE_COMPONENT

PROJECT_PATH = Path(settings.BASE_DIR)
LOCALE_PATH = Path(os.path.join(PROJECT_PATH, "locale"))
TEMP_CONTENT_PATH = Path(os.path.join(PROJECT_PATH, "tmp", "weblate"))
TEMP_LOCALE_CONTENT_PATH = Path(os.path.join(TEMP_CONTENT_PATH, "locale"))

HEADERS = {
    "Authorization": f"Token {WEBLATE_API_KEY}",
    "Content-Type": "application/json",
}
URL_LIST = [
    WEBLATE_URL,
    "translations",
    WEBLATE_PROJECT,
    WEBLATE_COMPONENT,
    "en",
    "units/",
]
LANGUAGES = [lang for lang in LanguagesEnum]


class WeblateGateway(BaseTranslationGateway):
    """Weblate module management"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WeblateGateway, cls).__new__(cls)
            cls.headers = HEADERS
            cls.url = os.path.join(*URL_LIST).replace("\\", "/")
            cls.base_url = "/".join(cls.url.split("/")[:-3]) + "/"
        return cls._instance

    def add_key(self, key: str, translation: str) -> bool:
        """Add new key to weblate"""
        data = {
            "key": key,
            "value": [translation],
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        return response.status_code == 200

    def delete_key(self, key: str):
        if wb_key := self.__search_key(key, "en"):
            delete_url = f'{WEBLATE_URL}/units/{wb_key["id"]}/'
            try:
                response = requests.delete(delete_url, headers=self.headers)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                logging.error(f'Error while deleting key "{key}": {e}')
                return
        return wb_key

    def update_key_labels(self, key: str, labels):
        """Update labels for a key. Only used in command."""
        key_id = self.__search_key(key, "en")["id"]
        url = f"{WEBLATE_URL}/units/{key_id}/"
        updated_data = {"labels": labels}
        response = requests.patch(url, json=updated_data, headers=self.headers)
        return response.status_code == 200

    def fetch_translation(self, key, lang):
        """Fetch translated text from Weblate"""
        translation = ""
        if wb_key := self.__search_key(key, lang):
            try:
                translation = wb_key["target"][0]
            except (KeyError, IndexError) as e:
                logging.error(f'Error while getting translation for key "{key}": {e}')
                return None
        return translation

    def __search_key(self, key: str, lang: str):
        language_url = f"{lang}/units/"
        url = f"{self.base_url}{language_url}"
        params = {"q": f"context:={key}"}
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            if res := data.get("results"):
                return res[0]
            logging.error(f'Key "{key}" not found in language "{lang}".')
        except requests.exceptions.RequestException as e:
            logging.error(f'Error in searching for key "{key}": {e}')
        except (KeyError, IndexError) as e:
            logging.error(f"Error in the response format from Weblate: {e}")

    def update_translation(self, key_id: int, target):
        """Update target for a key. Only used in command."""
        url = f"{WEBLATE_URL}/units/{key_id}/"
        data = {"state": 20, "target": target}
        response = requests.patch(url, headers=self.headers, json=data)
        return response.status_code == 200

    def create_translations_files(self):
        """Download and create translations files into locale directory"""
        self.__create_path_to_save(LANGUAGES)
        self.__download_files()
        file_paths = self.__get_all_files()
        self.__move_po_files_to_locale_directory(file_paths)
        self.__compile_messages()
        return True

    def __create_path_to_save(self, languages):
        TEMP_CONTENT_PATH.mkdir(parents=True, exist_ok=True)
        for lang in languages:
            lang_path = TEMP_LOCALE_CONTENT_PATH / lang
            lang_path.mkdir(parents=True, exist_ok=True)
        return True

    def __download_files(self, format="po"):
        for lang_code in LANGUAGES:
            language_url = f"{lang_code}/file/"
            url = f"{self.base_url}{language_url}"
            response = requests.get(url, headers=self.headers)
            response.encoding = "utf-8"
            if response.status_code == 200:
                po_content = response.text
                file_path = TEMP_LOCALE_CONTENT_PATH / f"{lang_code}" / "django.po"
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(po_content)
            else:
                print(f"Error downloading the .po file for language {lang_code}. Status code: {response.status_code}")

    def __get_all_files(self):
        file_paths = []
        for root, directories, files in os.walk(TEMP_LOCALE_CONTENT_PATH):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(Path(filepath))
        return file_paths

    def __move_po_files_to_locale_directory(self, file_paths):
        for file_path in file_paths:
            lang = file_path.parts[-2]
            new_path = os.path.join(LOCALE_PATH, lang, "LC_MESSAGES", "django.po")
            os.replace(file_path, new_path)
        return True

    def __compile_messages(self):
        with suppress(Exception):
            call_command("compilemessages", "--use-fuzzy")
        cache.clear()
        return True

    def create_and_translate_to_migrate(self, content_en: str, lang="en"):
        """Create keys in weblate migrated from lokalise"""
        language_url = f"{lang}/file/"
        url = f"{self.base_url}{language_url}"
        files = {"file": ("file.po", content_en, "text/richtext")}
        method = "add" if lang == "en" else "translate"
        conflicts = "replace-translated" if lang == "en" else "ignore"
        data = {
            "method": method,
            "fuzzy": "approve",
            "conflicts": conflicts,
            "author": "Weblate Admin",
            "email": "admin@familify.com",
        }
        response = requests.post(
            url,
            headers={"Authorization": f"Token {WEBLATE_API_KEY}"},
            files=files,
            data=data,
        )
        if response.status_code == 200:
            print(f"PO file uploaded for language {lang} into Weblate")
        else:
            print(f"Error {lang} - {response.status_code} - {response.text}")
