from rest_framework import viewsets, permissions
from ..models import Lapangan
from ..serializers import LapanganSerializer

class LapanganViewsSet(viewsets.ModelViewSet):
    queryset = Lapangan.objects.all()
    serializer_class = LapanganSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]