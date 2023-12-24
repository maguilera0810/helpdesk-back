# .\apps\authentication\models.py
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    external_code = models.CharField(max_length=50, blank=True)


class TechnicianProfile(models.Model):
    """ 
        Modelo para perfil de técnico
    """
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    # Lista de especialidades, o usar un modelo relacionado
    specialties = models.TextField()
    is_available = models.BooleanField(default=True)
