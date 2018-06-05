from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    ring_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'ring_set', 'date_joined')
