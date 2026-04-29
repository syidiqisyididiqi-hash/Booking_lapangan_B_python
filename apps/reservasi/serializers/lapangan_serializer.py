from rest_framework import serializers
from ..models import Lapangan

class LapanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lapangan
        fields = '__all__'