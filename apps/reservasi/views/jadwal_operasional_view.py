from rest_framework import viewsets, permissions
from ..models import JadwalOperasional
from ..serializers import JadwaloperasionalSerializer

class JadwalOperasionalViewSet(viewsets.ModelViewSet):
    queryset = JadwalOperasional.objects.all()
    serializer_class = JadwaloperasionalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
