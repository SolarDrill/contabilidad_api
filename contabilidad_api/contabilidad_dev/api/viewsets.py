from contabilidad_dev.models import *
from contabilidad_dev.api.serializers import *
from rest_framework import viewsets

class DeparmentsViewSet(viewsets.ModelViewSet):
    queryset = Deparments.objects.all()
    serializer_class = DeparmentsSerializer
    filterset_fields = '__all__'

class UnitsOfMeasurementViewSet(viewsets.ModelViewSet):
    queryset = UnitsOfMeasurement.objects.all()
    serializer_class = UnitsOfMeasurementSerializer
    filterset_fields = '__all__'

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    filterset_fields = '__all__'

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filterset_field = '__all__'
