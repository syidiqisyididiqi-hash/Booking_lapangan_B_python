from rest_framework import serializers
from ..models import JadwalOperasional

class JadwaloperasionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JadwalOperasional
        fields = '__all__'