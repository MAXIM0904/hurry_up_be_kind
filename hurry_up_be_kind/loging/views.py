from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from all_users.models import Ward, Philantropist
from .serializers import RegistrationSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class UserInfToken(APIView):
    def post(self, request):
        data = {
            'id': str(request.user.id),
            'name': str(request.user.username),
        }
        return Response(data, status=status.HTTP_201_CREATED)



class RegistrationUser(APIView):
    '''класс региcтрации пользователя'''
    permission_classes = (AllowAny,)


    def get(self, request, format=None):

        print('1')
        print(request.GET)
        context = {
            'user': request.user,
            'auth': request.auth
        }
        return Response(context)


    def post(self, request):
        serializer_form = RegistrationSerializer(data=request.data)
        serializer_form.is_valid(raise_exception=True)
        phone_number = serializer_form.validated_data['phone_number']
        if User.objects.filter(username=phone_number):
            return Response({'error': 'A user with such a phone already exists.'})

        user = User.objects.create_user(
            username=phone_number,
            first_name=serializer_form.validated_data['first_name'],
            last_name=serializer_form.validated_data['last_name'],
            password=serializer_form.validated_data['password'],
        )

        status = serializer_form.validated_data['status'].lower()

        if status == 'подопечный':
            Ward.objects.create(
                user_profile=user,
                phone=phone_number,
            )

        elif status == 'участник':
            Philantropist.object.create(
                user_profile = instance,
                phone = phone
            )

        token = Token.objects.create(user=instance)
        return Response({
            'token': token.key,
            'user_status': status,
            'username': phone
        })