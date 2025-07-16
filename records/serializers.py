from rest_framework import serializers
from .models import ArrivalRecord


class ArrivalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArrivalRecord
        fields = '__all__'
        