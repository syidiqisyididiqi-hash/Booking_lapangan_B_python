from rest_framework import serializers
# from django.utils import timezone
from ..models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        lapangan = data['lapangan']
        tanggal = data['tanggal']
        jam_mulai = data['jam_mulai']
        jam_selesai = data['jam_selesai']

        if jam_mulai >= jam_selesai:
            raise serializers.ValidationError("Jam selesai harus lebih besar dari jam mulai.")
        
        bentrok = Booking.objects.filter(
            lapangan=lapangan,
            tanggal=tanggal,
            jam_mulai__lt=jam_selesai,
            jam_selesai__gt=jam_mulai,
            status_booking__in=['menunggu', 'disetujui']
        ).exists()

        if bentrok:
            raise serializers.ValidationError("Jadwal bentrok dengan booking lain.")
        
        return data