from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from all_users.models import Ward, Philantropist
from .forms import SignupForm


class UserInfToken(APIView):
    def post(self, request):
        data = {
            'id': str(request.user.id),
            'name': str(request.user.username),
        }
        return Response(data, status=status.HTTP_201_CREATED)



class RegistrationUser(APIView):

    '''класс регитсрации пользователя'''

    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():
            phone = str(form.cleaned_data['phone'])
            if User.objects.filter(username=phone):
                return Response({'error': 'A user with such a phone already exists.'})
            instance = form.save(commit=False)
            instance.username = form.cleaned_data['phone']
            instance.save()
            status = form.cleaned_data['status']
            phone = form.cleaned_data['phone']

            if status == 'подопечный':
                Ward.objects.create(
                    user_profile = instance,
                    phone = phone
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

        else:
            return Response(form.errors)
