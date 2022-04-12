from rest_framework import serializers
from all_users.models import Philantropist


class SerializerPhilantropist(serializers.ModelSerializer):
    status = models.CharField(max_length=100, verbose_name='Имя пользователя')
    class Meta:
        model = Philantropist
        fields = ('name', 'phone',)
