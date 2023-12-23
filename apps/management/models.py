# .\apps\management\models.py
from django.db import models


class StateTask(models.Model):
    code = models.CharField(max_length=50, blank=True)


def get_default_state_task():
    state, _ = StateTask.objects.get_or_create(code='todo')
    return state.id


class Task(models.Model):
    main_user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    team = models.ManyToManyField('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    state = models.ForeignKey('management.StateTask',
                              on_delete=models.DO_NOTHING,
                              default=get_default_state_task)
    type = models.CharField(max_length=10, blank=True)
