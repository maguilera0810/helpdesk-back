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


def get_crud_route(model: str, view: BaseCRUDView):
    model = slugify(model)
    return [
        path(f"{model}/", view.as_view({**METHODS})),
        path(f"{model}/<int:id>/", view.as_view({**METHODS_ID})),
    ]
