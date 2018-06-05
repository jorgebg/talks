from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    date_joined = serializers.DateTimeField()

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        instance.date_joined = validated_data.get('date_joined')
        instance.save()
        return instance
