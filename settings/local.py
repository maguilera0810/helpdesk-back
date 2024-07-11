# .\settings\local.py
from settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    "django_extensions",
]
