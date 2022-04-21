from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User
from all_users.models import Ward, Philantropist
from .serializers import RegistrationSerializer, UserUpdateSerializer, PhilantropistUpdateSerializer, WardUpdateSerializer


class UserInfToken(APIView):
    '''Класс предоставляет доступ к данным пользователя'''
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user_inf = User.objects.get(username=request.user)

        try:
            user_inf_profile = Philantropist.objects.get(user_profile_id=request.user.id)
            context = {'username': user_inf.username,
                       'last_name': user_inf.last_name,
                       'first_name': user_inf.first_name,
                       'phone': user_inf_profile.phone,
                       'about_me_philantropist': user_inf_profile.about_me_philantropist,
                       'size_donations': user_inf_profile.size_donations,
                       'status': 'участник'
                       }

        except:
            user_inf_profile = Ward.objects.get(user_profile_id=request.user.id)
            context = {'username': user_inf.username,
                       'last_name': user_inf.last_name,
                       'first_name': user_inf.first_name,
                       'phone': user_inf_profile.phone,
                       'about_me_ward': user_inf_profile.about_me_ward,
                       'status': 'подопечный'
                       }
        return JsonResponse(context)


class RegistrationUser(APIView):
    '''класс региcтрации пользователя'''
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer_form = RegistrationSerializer(data=request.data)
        serializer_form.is_valid(raise_exception=True)
        phone_number = serializer_form.validated_data['phone_number']
        if User.objects.filter(username=phone_number):
            return JsonResponse({'error': 'A user with such a phone already exists.'})

        user = User.objects.create_user(
            username=phone_number,
            first_name=serializer_form.validated_data['first_name'],
            last_name=serializer_form.validated_data['last_name'],
            password=serializer_form.validated_data['password'],
        )

        status = serializer_form.validated_data['status'].lower()

        try:
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
        except Exception as err:
            user.delete()
            return JsonResponse({'error' : str(err)})

        token = Token.objects.create(user=user)
        return JsonResponse({
            'token': token.key,
        })


class Loging(ObtainAuthToken):
    '''Класс регистрации пользователя (получение токена)'''
    permission_classes = (AllowAny,)


class Logout(APIView):
    '''Класс отмены регистрации пользователя (удаление токена)'''
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        token = Token.objects.get(key=request.auth)
        token.delete()
        return JsonResponse({'status': 'status 200'})


class UserUpdateProfile(UpdateAPIView):
    '''Класс изменения данных пользователя'''
    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        user_form = UserUpdateSerializer(request.user, request.POST)
        user_form.is_valid(raise_exception=True)

        if Ward.objects.filter(user_profile_id=request.user.id):
            ward_profile = Ward.objects.get(user_profile_id=request.user.id)
            user_update_profile = WardUpdateSerializer(ward_profile, request.POST)

        elif Philantropist.objects.filter(user_profile_id=request.user.id):
            philantropist_profile = Philantropist.objects.get(user_profile_id=request.user.id)
            user_update_profile = PhilantropistUpdateSerializer(philantropist_profile, request.POST)

        else:
            return JsonResponse({'error': 'No record detected'})

        user_update_profile.is_valid(raise_exception=True)

        if user_update_profile.validated_data.get('phone'):
            print(user_update_profile.validated_data)
            request.user.username = user_update_profile.validated_data['phone']

        try:
            user_form.save()
            user_update_profile.save()
        except Exception as error:
            return JsonResponse({"1": str(error)})

        return JsonResponse({'status': 'status 200'})

class UserDelete(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_profile = User.objects.get(id=request.user.id)
        user_profile.delete()
        return JsonResponse({'status': 'status 200'})
