from django.db import models
from .booking import Booking

class Pembayaran(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    metode_bayar = models.CharField(max_length=50)
    jumlah_bayar = models.DecimalField(max_digits=10, decimal_places=2)
    status_bayar = models.CharField(max_length=20)
    tanggal_bayar = models.DateTimeField(auto_now_add=True)