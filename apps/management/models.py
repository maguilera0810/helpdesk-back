# .\apps\management\models.py
from typing import Union

from django.db import models

from apps.core.models import AuditModel, BaseInfoModel, PeriodModel
from utils.enums import TaskPriority, TaskStatus, TaskType


class MaintenancePlan(BaseInfoModel, PeriodModel):
    """
        Modelo para plan de mantenimiento
    """
    responsible = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,
                                    related_name='responsible_maintenance_plan')


class ScheduledTask(BaseInfoModel, AuditModel, PeriodModel):
    maintenance_plan = models.ForeignKey('management.MaintenancePlan', related_name='scheduled_tasks',
                                         on_delete=models.DO_NOTHING, null=False, blank=False)
    priority = models.CharField(max_length=50, choices=TaskPriority.choices,
                                default=TaskPriority.LOWEST)
    responsible = models.ForeignKey('auth.User', related_name='responsible_scheduled_tasks', on_delete=models.DO_NOTHING,
                                    null=True, blank=True, verbose_name='Responsible User')
    team = models.ManyToManyField('auth.User',
                                  related_name='assigned_scheduled_tasks')
    created_by = models.ForeignKey('auth.User', related_name='created_scheduled_tasks',
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    recurrence_rule = models.CharField(max_length=255)
    next_run_date = models.DateField()


class Task(BaseInfoModel, AuditModel):
    """
        Modelo para tareas de mantenimiento
    """
    type = models.CharField(max_length=50, choices=TaskType.choices,
                            default=TaskType.PREVENTIVE)
    status = models.CharField(max_length=50, choices=TaskStatus.choices,
                              default=TaskStatus.PENDING)
    priority = models.CharField(max_length=50, choices=TaskPriority.choices,
                                default=TaskPriority.LOWEST)
    responsible = models.ForeignKey('auth.User', related_name='responsible_tasks', on_delete=models.DO_NOTHING,
                                    null=True, blank=True, verbose_name='Responsible User')
    team = models.ManyToManyField('auth.User', related_name='assigned_tasks')
    created_by = models.ForeignKey('auth.User', related_name='created_tasks',
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    maintenance_plan = models.ForeignKey('management.MaintenancePlan', related_name='tasks',
                                         on_delete=models.DO_NOTHING, null=True, blank=True)
    scheduled = models.ForeignKey('management.ScheduledTask', on_delete=models.SET_NULL,
                                  related_name='scheduled_tasks', null=True, blank=True)


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
    status = models.CharField(max_length=50, choices=TaskStatus.choices)
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
    MaintenancePlan,
    ScheduledTask,
    Task,
    RequestingUnit,
    Request,
    TaskHistory,
    Report,
]
MODELS_TYPES = Union[
    MaintenancePlan,
    ScheduledTask,
    Task,
    RequestingUnit,
    Request,
    TaskHistory,
    Report,
]
