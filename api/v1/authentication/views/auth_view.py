from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from api.base.views import IsAuthenticatedView
from apps.authentication.dtos import AuthDTO
from apps.authentication.models import Profile
from apps.authentication.serializers import UserSerializer
from gateways.utmach import UTMACH
from apps.authentication.serializers import UserSerializer


class AuthView(IsAuthenticatedView):

    def login(self, request):
        """
        Method: POST
        """
        data = AuthDTO(**request.data)
        resp_status, resp_data = UTMACH.check_user(data)
        if resp_status != 200:
            return Response({'error': 'not_register'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=data.email)
        except User.DoesNotExist:
            user = User(email=data.email,
                        username=data.email.split('@')[0],
                        first_name=resp_status.get('first_name'),
                        last_name=resp_status.get('last_name'))
            user.save()
            # TODO serilizar resp_data a los campos de PRofile
            profile = Profile(user=user, **resp_data)
            profile.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
