from django.core.management.base import BaseCommand

from apps.authentication.models import Permission

group_dashboard = "support_dashboard"
group_tracking = "support_tracking"
group_task = "support_task"
group_issue = "support_issue"
group_user = "admin_user"
group_role = "admin_role"
group_profile = "settings_profile"
group_category = "settings_category"
group_priority = "settings_priority"

PERMISSIONS = [
    {"group": group_dashboard, "key": "dashboard_see", "title": "Ver Tablero"},
    {"group": group_tracking, "key": "tracking_see", "title": "Ver Seguimiento"},

    {"group": group_task, "key": "task_list", "title": "Listar Tareas"},
    {"group": group_task, "key": "task_see", "title": "Ver Tarea"},
    {"group": group_task, "key": "task_create", "title": "Crear Tarea"},
    {"group": group_task, "key": "task_update", "title": "Actualizar Tarea"},
    {"group": group_task, "key": "task_update_status",
        "title": "Actualizar Estado Tarea"},

    {"group": group_issue, "key": "issue_list", "title": "Listar Problemas"},
    {"group": group_issue, "key": "issue_see", "title": "Ver Problema"},
    {"group": group_issue, "key": "issue_create", "title": "Crear Problema"},
    {"group": group_issue, "key": "issue_update", "title": "Actualizar Problema"},
    {"group": group_issue, "key": "issue_update_status",
        "title": "Actualizar Estado Problema"},
    {"group": group_issue, "key": "issue_create_task",
        "title": "Crear Tarea desde Problema"},

    {"group": group_user, "key": "user_list", "title": "Listar Usuarios"},
    {"group": group_user, "key": "user_see", "title": "Ver Usuario"},
    {"group": group_user, "key": "user_create", "title": "Crear Usuario"},
    {"group": group_user, "key": "user_update", "title": "Actualizar Usuario"},
    {"group": group_user, "key": "user_reset_pw",
        "title": "Restablecer Contraseña Usuario"},
    {"group": group_user, "key": "user_create_task",
        "title": "Crear Tarea para Usuario"},
    {"group": group_user, "key": "user_update_role",
        "title": "Actualizar Roles Usuario"},

    {"group": group_role, "key": "role_list", "title": "Listar Roles"},
    {"group": group_role, "key": "role_see", "title": "Ver Rol"},
    {"group": group_role, "key": "role_create", "title": "Crear Rol"},
    {"group": group_role, "key": "role_update", "title": "Actualizar Rol"},

    {"group": group_profile, "key": "profile_see", "title": "Ver Perfil"},
    {"group": group_profile, "key": "profile_update", "title": "Actualizar Perfil"},
    {"group": group_profile, "key": "profile_reset_pw",
        "title": "Restablecer Contraseña Perfil"},
    {"group": group_profile, "key": "profile_update_pw",
        "title": "Actualizar Contraseña Perfil"},

    {"group": group_category, "key": "category_list", "title": "Listar Categorías"},
    {"group": group_category, "key": "category_see", "title": "Ver Categoría"},
    {"group": group_category, "key": "category_create", "title": "Crear Categoría"},
    {"group": group_category, "key": "category_update",
        "title": "Actualizar Categoría"},
    {"group": group_category, "key": "category_update_status",
        "title": "Actualizar Estado Categoría"},

    {"group": group_priority, "key": "priority_list", "title": "Listar Prioridades"},
    {"group": group_priority, "key": "priority_see", "title": "Ver Prioridad"},
    {"group": group_priority, "key": "priority_create", "title": "Crear Prioridad"},
    {"group": group_priority, "key": "priority_update",
        "title": "Actualizar Prioridad"},
    {"group": group_priority, "key": "priority_update_status",
        "title": "Actualizar Estado Prioridad"}
]


class Command(BaseCommand):
    help = "upsert permissions on db"

    def handle(self, *args, **kwargs):
        for p in PERMISSIONS:
            key = p["key"]
            title = p["title"]
            group = p["group"]
            is_updated = False
            if permission := Permission.objects.filter(key=key).first():
                if permission.group != group:
                    permission.group = group
                    is_updated = True
                if permission.title != title:
                    permission.title = title
                    is_updated = True
                if is_updated:
                    msg = f"Permiso Actualizado: {key} - {title}"
                    permission.save()
                else:
                    msg = f"Permiso ya existe: {key} - {title}"
            else:
                permission = Permission(key=key,
                                        title=title)
                msg = f"Permiso Creeado: {key} - {title}"
                permission.save()
            self.stdout.write(self.style.WARNING(msg))
