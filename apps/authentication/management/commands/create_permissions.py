from django.core.management.base import BaseCommand

from apps.authentication.models import Permission

PERMISSIONS = [
    {"key": "dashboard_see", "title": "Ver Tablero"},

    {"key": "tracking_see", "title": "Ver Seguimiento"},

    {"key": "task_list", "title": "Listar Tareas"},
    {"key": "task_see", "title": "Ver Tarea"},
    {"key": "task_create", "title": "Crear Tarea"},
    {"key": "task_update", "title": "Actualizar Tarea"},
    {"key": "task_update_status", "title": "Actualizar Estado Tarea"},

    {"key": "issue_list", "title": "Listar Problemas"},
    {"key": "issue_see", "title": "Ver Problema"},
    {"key": "issue_create", "title": "Crear Problema"},
    {"key": "issue_update", "title": "Actualizar Problema"},
    {"key": "issue_update_status", "title": "Actualizar Estado Problema"},
    {"key": "issue_create_task", "title": "Crear Tarea desde Problema"},

    {"key": "user_list", "title": "Listar Usuarios"},
    {"key": "user_see", "title": "Ver Usuario"},
    {"key": "user_create", "title": "Crear Usuario"},
    {"key": "user_update", "title": "Actualizar Usuario"},
    {"key": "user_reset_pw", "title": "Restablecer Contraseña Usuario"},
    {"key": "user_create_task", "title": "Crear Tarea para Usuario"},
    {"key": "user_update_role", "title": "Actualizar Roles Usuario"},

    {"key": "role_list", "title": "Listar Roles"},
    {"key": "role_see", "title": "Ver Rol"},
    {"key": "role_create", "title": "Crear Rol"},
    {"key": "role_update", "title": "Actualizar Rol"},

    {"key": "profile_see", "title": "Ver Perfil"},
    {"key": "profile_update", "title": "Actualizar Perfil"},
    {"key": "profile_reset_pw", "title": "Restablecer Contraseña Perfil"},
    {"key": "profile_update_pw", "title": "Actualizar Contraseña Perfil"},

    {"key": "category_list", "title": "Listar Categorías"},
    {"key": "category_see", "title": "Ver Categoría"},
    {"key": "category_create", "title": "Crear Categoría"},
    {"key": "category_update", "title": "Actualizar Categoría"},
    {"key": "category_update_status", "title": "Actualizar Estado Categoría"},

    {"key": "priority_list", "title": "Listar Prioridades"},
    {"key": "priority_see", "title": "Ver Prioridad"},
    {"key": "priority_create", "title": "Crear Prioridad"},
    {"key": "priority_update", "title": "Actualizar Prioridad"},
    {"key": "priority_update_status", "title": "Actualizar Estado Prioridad"}
]


class Command(BaseCommand):
    help = "upsert permissions on db"

    def handle(self, *args, **kwargs):
        for p in PERMISSIONS:
            key = p["key"]
            title = p["title"]
            if permission := Permission.objects.filter(key=key).first():
                if permission.title != title:
                    permission.title = title
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
