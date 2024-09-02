# .\api\core\routes.py
from django.urls import path
from django.utils.text import slugify

from api.core.views.base_crud_view import BaseCRUDView

METHODS = {
    "get": "list",
    "post": "create",
}
METHODS_ID = {
    "get": "retrieve",
    "put": "update",
    "delete": "destroy",
}
METHODS_FILE = {
    "put": "update_files",
}


def get_crud_route(model: str, view: BaseCRUDView, has_files: bool = False):
    model = slugify(model)
    paths = [
        path(f"{model}/", view.as_view(METHODS)),
        path(f"{model}/<int:id>/", view.as_view(METHODS_ID)),
    ]
    if has_files:
        paths += [
            path(f"{model}/<int:id>/files/", view.as_view(METHODS_FILE)),
        ]
    return paths
