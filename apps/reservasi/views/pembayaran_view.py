from rest_framework import viewsets, permissions
from ..models import Pembayaran
from ..serializers import PembayaranSerializer

class PembayaranViewSet(viewsets.ModelViewSet):
    queryset = Pembayaran.objects.all()
    serializer_class = PembayaranSerializer
    permission_classes = [permissions.IsAuthenticated]