from rest_framework import serializers
from ..models import LogStatus

class LogStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogStatus
        fields = '__all__'