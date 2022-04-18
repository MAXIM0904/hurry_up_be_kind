from rest_framework import serializers
from all_users.models import Philantropist, Ward


class SerializerPhilantropist(serializers.ModelSerializer):
    class Meta:
        model = Philantropist
        fields = '__all__'


class SerializerWard(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'