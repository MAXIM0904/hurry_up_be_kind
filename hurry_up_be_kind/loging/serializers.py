from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    ''' Сериализация регистрации нового пользователя '''

    password1 = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)
    status = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=25, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'password1', 'password2', 'status')
