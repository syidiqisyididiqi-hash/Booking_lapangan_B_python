from rest_framework.routers import DefaultRouter

from .views import (
    LapanganViewsSet,
    JadwalOperasionalViewSet,
    BookingViewSet,
    PembayaranViewSet,
    LogStatusViewSet,
)

router = DefaultRouter()
router.register(r'lapangan', LapanganViewsSet)
router.register(r'jadwal-operasional', JadwalOperasionalViewSet)
router.register(r'booking', BookingViewSet)
router.register(r'pembayaran', PembayaranViewSet)
router.register(r'log-status', LogStatusViewSet)

urlpatterns = router.urls