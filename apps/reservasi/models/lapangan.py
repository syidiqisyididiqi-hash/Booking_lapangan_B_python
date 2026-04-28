from django.db import models

class Lapangan(models.Model):
    nama_lapangan = models.CharField(max_length=100)
    jenis_olahraga = models.CharField(max_length=100)
    harga_per_jam = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nama_lapangan