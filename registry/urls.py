from rest_framework.routers import DefaultRouter

from registry.resources import RegistryViewSet

router = DefaultRouter()
router.register(r'', RegistryViewSet, basename='registry')
urlpatterns = router.urls
