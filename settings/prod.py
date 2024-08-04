# .\settings\prod.py
from settings.base import *

DEBUG = config("DEBUG", cast=bool, default=False)

USE_BASIC_AUTH = config("USE_BASIC_AUTH", cast=bool, default=False)
if USE_BASIC_AUTH:
    SWAGGER_SETTINGS["SECURITY_DEFINITIONS"]["Basic"] = {
        'type': 'basic',
        'name': 'Bearer',
        'in': 'header'
    }

ALLOWED_HOSTS = ['*']
