from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Philantropist(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия пользователя')
    about_me_philantropist = models.TextField(verbose_name="О себе")
    size_donations = models.IntegerField(default=0, verbose_name='Размер пожертвований')
    phone = PhoneNumberField()
    registrarion_date_philantropist = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.surname


class Ward(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя подопечного')
    surname = models.CharField(max_length=100, verbose_name='Фамилия подопечного')
    size_donations = models.IntegerField(default=0, verbose_name='Размер пожертвований')
    about_me_ward = models.TextField(verbose_name="О себе")
    phone = PhoneNumberField()
    registrarion_date_ward = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.surname
