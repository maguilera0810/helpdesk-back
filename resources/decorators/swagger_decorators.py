from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.serializers import ModelSerializer


def custom_swagger_schema(serializer_class: ModelSerializer):
    _RESPONSES = {
        status.HTTP_201_CREATED: serializer_class(),
        status.HTTP_400_BAD_REQUEST: "BAD_REQUEST",
        status.HTTP_404_NOT_FOUND: "NOT_FOUND",
        status.HTTP_204_NO_CONTENT: "NO_CONTENT",
    }
    model = serializer_class.Meta.model
    model_name = model.__name__
    app_name = model._meta.app_label

    def swagger_schema(action: str, responses: dict[int, any] = None, tag: str = ""):
        if not responses:
            responses = {}
        RESPONSES = {status.HTTP_200_OK: serializer_class(many=True) if action else serializer_class(),
                     **_RESPONSES}

        def decorator(func):
            operation_description = ""
            _responses = {}
            request_body = None
            if action == "list":
                operation_description = f"Retrieve a list of all {model_name}s"
                _responses = {
                    status.HTTP_200_OK: RESPONSES[status.HTTP_200_OK],
                }
            elif action == "create":
                operation_description = f"Create a new {model_name}"
                _responses = {
                    status.HTTP_201_CREATED: RESPONSES[status.HTTP_201_CREATED],
                    status.HTTP_400_BAD_REQUEST: RESPONSES[status.HTTP_400_BAD_REQUEST],
                }
                request_body = serializer_class
            elif action == "retrieve":
                operation_description = f"Retrieve a {model_name} by ID"
                _responses = {
                    status.HTTP_200_OK: RESPONSES[status.HTTP_200_OK],
                    status.HTTP_404_NOT_FOUND: RESPONSES[status.HTTP_404_NOT_FOUND],
                }

            elif action == "update":
                operation_description = f"Update a specific {model_name} by ID"
                _responses = {
                    status.HTTP_200_OK: RESPONSES[status.HTTP_200_OK],
                    status.HTTP_400_BAD_REQUEST: RESPONSES[status.HTTP_400_BAD_REQUEST],
                    status.HTTP_404_NOT_FOUND: RESPONSES[status.HTTP_404_NOT_FOUND],
                }
                request_body = serializer_class
            elif action == "destroy":
                operation_description = f"Delete a specific {model_name} by ID"
                _responses = {
                    status.HTTP_204_NO_CONTENT: RESPONSES[status.HTTP_204_NO_CONTENT],
                    status.HTTP_400_BAD_REQUEST: RESPONSES[status.HTTP_400_BAD_REQUEST],
                    status.HTTP_404_NOT_FOUND: RESPONSES[status.HTTP_404_NOT_FOUND],
                }

            elif action == "update_files":
                operation_description = f"Update files for a specific {model_name} by ID"
                _responses = {
                    status.HTTP_200_OK: RESPONSES[status.HTTP_200_OK],
                    status.HTTP_400_BAD_REQUEST: RESPONSES[status.HTTP_400_BAD_REQUEST],
                    status.HTTP_404_NOT_FOUND: RESPONSES[status.HTTP_404_NOT_FOUND],
                }
            swagger_auto_schema(operation_description=operation_description,
                                tags=[tag or f"{app_name}.{model_name}"],
                                request_body=request_body,
                                responses={**_responses, **responses})(func)
            return func

        return decorator
    return swagger_schema
