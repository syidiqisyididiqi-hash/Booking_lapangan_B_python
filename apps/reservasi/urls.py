from rest_framework.routers import DefaultRouter

from .views import (
    LapanganViewsSet,
    JadwalOperasionalViewSet,
)

router = DefaultRouter()
router.register(r'lapangan', LapanganViewsSet)
router.register(r'jadwal-operasional', JadwalOperasionalViewSet)

urlpatterns = router.urls