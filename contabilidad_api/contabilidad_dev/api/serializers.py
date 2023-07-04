from contabilidad_dev.models import *
from rest_framework import serializers

class DeparmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deparments
        fields = '__all__'

class UnitsOfMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitsOfMeasurement
        fields = '__all__'

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
