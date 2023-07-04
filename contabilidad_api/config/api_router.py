from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from contabilidad_dev.api.viewsets import UnitsOfMeasurementViewSet, DeparmentsViewSet, ItemsViewSet, SupplierViewSet
from contabilidad_api.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("units", UnitsOfMeasurementViewSet)
router.register("departments", DeparmentsViewSet)
router.register("items", ItemsViewSet)
router.register("suppliers", SupplierViewSet)


app_name = "api"
urlpatterns = router.urls
