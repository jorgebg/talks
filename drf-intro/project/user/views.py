from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import UserSerializer


class UserViewSet(ViewSet):

    def list(self, request):
        users = User.objects.all()
        ser = UserSerializer(users, many=True)
        return Response(ser.data)

    def create(self, request):
        ser = UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(status=201)
        return Response(status=400)

    def retrieve(self, request):
        user = User.objects.get(pk=request)
        ser = UserSerializer(user)
        return Response(ser.data)
