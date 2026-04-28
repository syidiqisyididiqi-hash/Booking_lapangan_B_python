from django.db import models
from .lapangan import Lapangan

class JadwalOperasional(models.Model):
    HARI = [
        ('Senin','Senin'), ('Selasa','Selasa'), ('Rabu','Rabu'),
        ('Kamis','Kamis'), ('Jumat','Jumat'),
        ('Sabtu','Sabtu'), ('Minggu','Minggu'),
    ]

    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)
    hari = models.CharField(max_length=10, choices=HARI)
    jam_buka = models.TimeField()
    jam_tutup = models.TimeField()