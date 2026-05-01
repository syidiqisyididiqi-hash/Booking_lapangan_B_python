from rest_framework.routers import DefaultRouter


from .views import (
    LapanganViewsSet,
)

router = DefaultRouter()
router.register(r'lapangan', LapanganViewsSet)