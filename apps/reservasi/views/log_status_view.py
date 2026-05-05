from rest_framework import viewsets, permissions
from ..models import LogStatus
from ..serializers import LogStatusSerializer

class LogStatusViewSet(viewsets.ModelViewSet):
    queryset = LogStatus.objects.all()
    serializer_class = LogStatusSerializer
    permission_classes = [permissions.IsAuthenticated]