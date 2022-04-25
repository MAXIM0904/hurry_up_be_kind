from rest_framework import serializers
from django.contrib.auth.models import User
from all_users.models import Philantropist, Ward


class RegistrationSerializer(serializers.ModelSerializer):
    ''' Сериализация регистрации нового пользователя '''

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    status = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=25, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'password', 'status')


class UserUpdateSerializer(serializers.ModelSerializer):
    ''' Сериализация изменения данных профиля User '''
    class Meta:
        model = User
        fields = ('last_name', 'first_name')


class PhilantropistUpdateSerializer(serializers.ModelSerializer):
    ''' Сериализация изменения данных профиля Philantropist '''
    class Meta:
        model = Philantropist
        fields = '__all__'


class WardUpdateSerializer(serializers.ModelSerializer):
    ''' Сериализация изменения данных профиля Ward '''
    class Meta:
        model = Ward
        fields = '__all__'
