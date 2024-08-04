# .\settings\local.py
from settings.base import *

DEBUG = config("DEBUG", cast=bool, default=True)

USE_BASIC_AUTH = onfig("USE_BASIC_AUTH", cast=bool, default=True)
if USE_BASIC_AUTH:
    SWAGGER_SETTINGS["SECURITY_DEFINITIONS"]["Basic"] = {
        "type": "basic",
        "name": "Bearer",
        "in": "header"
    }

ALLOWED_HOSTS = ["*"]
