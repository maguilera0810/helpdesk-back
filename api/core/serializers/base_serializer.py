from rest_framework.serializers import ModelSerializer, ValidationError


class BaseSerializer(ModelSerializer):

    def validate_request_user(self):
        request = self.context.get("request")
        if not request:
            raise ValidationError({"request": "no_request"})
        request_user = request.user
        if not request_user:
            raise ValidationError({"user": "no_request_user"})
        return request_user

    def validate(self, data: dict):
        self.validate_request_user()
        return data
