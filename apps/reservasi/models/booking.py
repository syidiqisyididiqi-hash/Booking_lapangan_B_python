from django.db import models
from django.contrib.auth.models import User
from .lapangan import Lapangan

class Booking(models.Model):
    STATUS = [
        ('menunggu','Menunggu'),
        ('lunas','Lunas'),
        ('batal','Batal'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)
    tanggal = models.DateField()
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    status_booking = models.CharField(max_length=20, choices=STATUS, default='menunggu')