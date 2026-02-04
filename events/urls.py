from rest_framework.routers import DefaultRouter

from .views import EventViewSet, EventImageViewSet


router = DefaultRouter()
router.register(r'events', EventViewSet, basename='events')
router.register(r'events-images', EventImageViewSet, basename='events-images')

urlpatterns = router.urls