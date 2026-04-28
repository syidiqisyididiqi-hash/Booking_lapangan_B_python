from django.contrib import admin
from .models import Lapangan, JadwalOperasional, Booking, Pembayaran, LogStatus

# Register your models here.
admin.site.register(Lapangan)
admin.site.register(JadwalOperasional)
admin.site.register(Booking)
admin.site.register(Pembayaran)
admin.site.register(LogStatus)
