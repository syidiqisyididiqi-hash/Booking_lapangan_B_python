from rest_framework.routers import DefaultRouter

from .views import (
    LapanganViewsSet,
    JadwalOperasionalViewSet,
    BookingViewSet,
)

router = DefaultRouter()
router.register(r'lapangan', LapanganViewsSet)
router.register(r'jadwal-operasional', JadwalOperasionalViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = router.urls