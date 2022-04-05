from rest_framework import serializers
from all_users.models import Philantropist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Philantropist
        fields = '__all__'
