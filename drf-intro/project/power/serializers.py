from rest_framework import serializers
from .models import Ring


class RingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = ('title',)
