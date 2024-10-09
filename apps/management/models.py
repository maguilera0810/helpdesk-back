# .\apps\management\models.py
from typing import Union

from django.db import models

from apps.core.models import (AuditModel, BaseInfoModel, BaseModel,
                              PeriodDateModel, PeriodDateTimeModel,
                              StorageModel)
from resources.enums import (IssueStatusEnum, TaskPriorityEnum, TaskStatusEnum,
                             TaskTypeEnum)

MODEL_TASK = "management.Task"


class Plan(BaseInfoModel, PeriodDateModel):
    """
        Modelo para plan de mantenimiento
    """
    responsible = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING,
                                    related_name="plans")


class Task(BaseInfoModel, AuditModel, PeriodDateTimeModel):
    """
        Modelo para tareas de mantenimiento
    """
    code = models.CharField(max_length=37, editable=False, blank=False,
                            db_index=True,  unique=True, help_text="max_length= len(model_name) + 33")
    type = models.CharField(max_length=50, choices=TaskTypeEnum.choices,
                            default=TaskTypeEnum.PREVENTIVE)
    status = models.CharField(max_length=50, choices=TaskStatusEnum.choices,
                              default=TaskStatusEnum.TO_DO)
    # priority = models.ForeignKey("common.Priority",
    #                              on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey("auth.User", related_name="created_tasks",
                                   on_delete=models.DO_NOTHING, null=False, editable=False)
    responsible = models.ForeignKey("auth.User", related_name="responsible_tasks",
                                    on_delete=models.DO_NOTHING, null=True, blank=True)
    team = models.ManyToManyField("auth.User", related_name="assigned_tasks",
                                  blank=True)
    plan = models.ForeignKey("management.Plan", related_name="tasks",
                             on_delete=models.DO_NOTHING, null=True)
    categories = models.ManyToManyField("common.Category", blank=True,
                                        related_name="tasks")


class Issue(BaseInfoModel, AuditModel):
    code = models.CharField(max_length=38, editable=False, blank=False,
                            db_index=True,  unique=True, help_text="max_length= len(model_name) + 33")
    task = models.OneToOneField(MODEL_TASK, on_delete=models.DO_NOTHING,
                                null=True, blank=True, related_name="issue")
    categories = models.ManyToManyField("common.Category", blank=True,
                                        related_name="issues")
    status = models.CharField(max_length=50, choices=IssueStatusEnum.choices,
                              default=IssueStatusEnum.RECEIVED)
    created_by = models.ForeignKey("auth.User", related_name="created_issues",
                                   on_delete=models.DO_NOTHING, editable=False)
    contact_email = models.CharField(max_length=100, blank=True)
    contact_phone = models.CharField(max_length=10, blank=True)


class IssueFile(BaseInfoModel, AuditModel, StorageModel):
    issue = models.ForeignKey("management.Issue", on_delete=models.CASCADE,
                              related_name="files")
    file = models.CharField(max_length=200)
    created_by = models.ForeignKey("auth.User", related_name="created_issue_files",
                                   on_delete=models.DO_NOTHING, editable=False)


class ScheduledTask(BaseInfoModel, AuditModel, PeriodDateModel):
    plan = models.ForeignKey("management.Plan", related_name="scheduled_tasks",
                             on_delete=models.DO_NOTHING, null=False, blank=False)
    priority = models.CharField(max_length=50, choices=TaskPriorityEnum.choices,
                                default=TaskPriorityEnum.MEDIUM)
    responsible = models.ForeignKey("auth.User", related_name="responsible_scheduled_tasks", on_delete=models.DO_NOTHING,
                                    null=True, blank=True, verbose_name="Responsible User")
    team = models.ManyToManyField("auth.User",
                                  related_name="assigned_scheduled_tasks")
    created_by = models.ForeignKey("auth.User", related_name="created_scheduled_tasks",
                                   on_delete=models.DO_NOTHING, editable=False)
    recurrence_rule = models.CharField(max_length=255)
    next_run_date = models.DateField()


class TaskComment(AuditModel):
    task = models.ForeignKey(MODEL_TASK, related_name="comments", on_delete=models.CASCADE,
                             null=True, blank=True)
    author = models.ForeignKey("auth.User", related_name="comments", on_delete=models.DO_NOTHING,
                               null=True, blank=True)
    content = models.TextField(blank=True)
    files = models.JSONField(default=list)


class RequestingUnit(BaseInfoModel):
    """
        Modelo para unidades requirentes (facultades, departamentos, etc.)
    """
    administrator = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING,
                                      related_name="administered_units")


class TaskHistory(BaseModel):
    """ 
        Modelo para historial de tareas
    """
    task = models.ForeignKey(MODEL_TASK, on_delete=models.DO_NOTHING,
                             related_name="history")
    status = models.CharField(max_length=50, choices=TaskStatusEnum.choices)
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING,
                                   related_name="task_changes")


class Report(AuditModel):
    """
        Modelo para informes
    """
    task = models.ForeignKey(MODEL_TASK, on_delete=models.DO_NOTHING,
                             related_name="reports")
    content = models.TextField()


MANAGEMENT_MODELS = [
    Plan,
    Issue,
    IssueFile,
    Report,
    RequestingUnit,
    ScheduledTask,
    Task,
    TaskHistory,
]
MANAGEMENT_MODEL_TYPES = Union[
    Plan,
    Issue,
    IssueFile,
    Report,
    RequestingUnit,
    ScheduledTask,
    Task,
    TaskHistory,
]
