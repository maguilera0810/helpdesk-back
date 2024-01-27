# .\apps\authentication\models.py
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    is_available = models.BooleanField(default=True)
    external_code = models.CharField(max_length=50, blank=True)
    # skills = models.ManyToManyField('authentication.Field')
