from rest_framework import viewsets, permissions
from ..models import Booking
from ..serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if getattr(user, 'role', None) == 'admin' or user.is_staff:
            return Booking.objects.all().order_by('-tanggal', '-jam_mulai')

        return Booking.objects.filter(user=user).order_by('-tanggal', '-jam_mulai')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)