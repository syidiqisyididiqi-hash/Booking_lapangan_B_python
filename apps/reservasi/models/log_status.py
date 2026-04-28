from django.db import models

class LogStatus(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    waktu_perubahan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.status} - {self.waktu_perubahan}"