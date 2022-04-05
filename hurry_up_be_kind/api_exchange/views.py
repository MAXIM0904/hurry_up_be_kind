from all_users.models import Philantropist
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Philantropist.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)
