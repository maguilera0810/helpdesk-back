# .\apps\management\models.py
from typing import Union
from uuid import uuid4

from django.db import models

from apps.core.models import AuditModel, BaseInfoModel, PeriodModel
from resources.enums import TaskPriorityEnum, TaskStatusEnum, TaskTypeEnum


class Plan(BaseInfoModel, PeriodModel):
    """
        Modelo para plan de mantenimiento
    """
    responsible = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,
                                    related_name='plans')


class Task(BaseInfoModel, AuditModel):
    """
        Modelo para tareas de mantenimiento
    """
    code = models.UUIDField(default=uuid4, editable=False)
    type = models.CharField(max_length=50, choices=TaskTypeEnum.choices,
                            default=TaskTypeEnum.PREVENTIVE)
    status = models.CharField(max_length=50, choices=TaskStatusEnum.choices,
                              default=TaskStatusEnum.TO_DO)
    priority = models.CharField(max_length=50, choices=TaskPriorityEnum.choices,
                                default=TaskPriorityEnum.MEDIUM)
    created_by = models.ForeignKey("auth.User", related_name="created_tasks",
                                   on_delete=models.DO_NOTHING, null=False, editable=False)
    responsible = models.ForeignKey("auth.User", related_name="responsible_tasks", on_delete=models.DO_NOTHING,
                                    null=False, blank=True)
    team = models.ManyToManyField("auth.User", related_name="assigned_tasks",
                                   blank=True)
    plan = models.ForeignKey("management.Plan", related_name="tasks",
                             on_delete=models.DO_NOTHING, null=True)
    scheduled = models.ForeignKey("management.ScheduledTask", on_delete=models.SET_NULL,
                                  related_name="scheduled_tasks", null=True, blank=True)


class ScheduledTask(BaseInfoModel, AuditModel, PeriodModel):
    plan = models.ForeignKey('management.Plan', related_name='scheduled_tasks',
                             on_delete=models.DO_NOTHING, null=False, blank=False)
    priority = models.CharField(max_length=50, choices=TaskPriorityEnum.choices,
                                default=TaskPriorityEnum.MEDIUM)
    responsible = models.ForeignKey('auth.User', related_name='responsible_scheduled_tasks', on_delete=models.DO_NOTHING,
                                    null=True, blank=True, verbose_name='Responsible User')
    team = models.ManyToManyField('auth.User',
                                  related_name='assigned_scheduled_tasks')
    created_by = models.ForeignKey('auth.User', related_name='created_scheduled_tasks',
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    recurrence_rule = models.CharField(max_length=255)
    next_run_date = models.DateField()


class TaskComment(AuditModel):
    task = models.ForeignKey('management.Task', related_name='comments', on_delete=models.CASCADE,
                             null=True, blank=True)
    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.DO_NOTHING,
                               null=True, blank=True)
    content = models.TextField(blank=True)
    files = models.JSONField(default=list)


class RequestingUnit(BaseInfoModel):
    """
        Modelo para unidades requirentes (facultades, departamentos, etc.)
    """
    administrator = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,
                                      related_name='administered_units')


class Request(models.Model):
    """
        Modelo para solicitudes
    """
    requesting_unit = models.ForeignKey('management.RequestingUnit', on_delete=models.CASCADE,
                                        related_name='requests')
    task = models.OneToOneField('management.Task', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class TaskHistory(models.Model):
    """ 
        Modelo para historial de tareas
    """
    task = models.ForeignKey('management.Task', on_delete=models.DO_NOTHING,
                             related_name='history')
    status = models.CharField(max_length=50, choices=TaskStatusEnum.choices)
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,
                                   related_name='task_changes')


class Report(AuditModel):
    """
        Modelo para informes
    """
    task = models.ForeignKey('management.Task', on_delete=models.DO_NOTHING,
                             related_name='reports')
    content = models.TextField()


MODELS = [
    Plan,
    ScheduledTask,
    Task,
    RequestingUnit,
    Request,
    TaskHistory,
    Report,
]
MODEL_TYPES = Union[
    Plan,
    ScheduledTask,
    Task,
    RequestingUnit,
    Request,
    TaskHistory,
    Report,
]
