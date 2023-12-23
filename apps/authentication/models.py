# .\apps\authentication\models.py
from django.db import models


class UserData(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    external_code = models.CharField(max_length=50, blank=True)
    # TODO agregar mas datos extra de los usuarios
