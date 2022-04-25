from all_users.models import Philantropist, Ward
from .serializers import SerializerPhilantropist, SerializerWard
from rest_framework.views import APIView
from rest_framework.response import Response


class PhilantropistList(APIView):
    def get(self, request, format=None):
        print('1')
        list_philantropist = Philantropist.objects.all()
        serializer = SerializerPhilantropist(list_philantropist, many=True)
        return Response(serializer.data)


class WardList(APIView):
    def get(self, request, format=None):
        list_ward = Ward.objects.all()
        serializer = SerializerWard(list_ward, many=True)
        return Response(serializer.data)
