from django.db import models
from django.contrib.auth.models import User


class Philantropist(models.Model):
    user_profile = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile_philantropist')
    about_me_philantropist = models.TextField(verbose_name="О себе", blank=True)
    size_donations = models.IntegerField(default=0, verbose_name='Размер пожертвований')
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", blank=True)
    registrarion_date_philantropist = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return str(self.user_profile)


class Ward(models.Model):
    user_profile = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile_ward')
    about_me_ward = models.TextField(verbose_name="О себе", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", blank=True)
    registrarion_date_ward = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    address_ward = models.TextField(default='', verbose_name='Адрес проживания')

    def __str__(self):
        return str(self.user_profile)
