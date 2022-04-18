from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from all_users.models import Ward, Philantropist
from .serializers import RegistrationSerializer


class UserInfToken(APIView):
    '''Класс предоставляет доступ к данным пользователя'''
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        print(request.user)
        print(request.user.id)
        user_inf = User.objects.get(username=request.user)

        try:
            user_inf_ptofile = Philantropist.objects.get(user_profile_id=request.user.id)
            return Response({
                'username': user_inf.username,
                'last_name': user_inf.last_name,
                'first_name': user_inf.first_name,
                'phone': user_inf_ptofile.phone,
                'about_me_philantropist': user_inf_ptofile.about_me_philantropist,
                'size_donations': user_inf_ptofile.size_donations,
                'status': 'участник'
            })

        except:
            user_inf_ptofile = Ward.objects.get(user_profile_id=request.user.id)

        return Response({
            'username': user_inf.username,
            'last_name': user_inf.last_name,
            'first_name': user_inf.first_name,
            'phone': user_inf_ptofile.phone,
            'about_me_ward': user_inf_ptofile.about_me_ward,
            'status': 'подопечный'
        })


class RegistrationUser(APIView):
    '''класс региcтрации пользователя'''
    permission_classes = (AllowAny,)

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
            Philantropist.objects.create(
                user_profile = user,
                phone = phone_number,
            )

        token = Token.objects.create(user=user)
        return Response({
            'token': token.key,
            'user_status': status,
            'username': phone_number,
        })
