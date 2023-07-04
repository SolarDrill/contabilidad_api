from django.contrib import admin
from contabilidad_dev.models import *
# Register your models here.

@admin.register(Deparments)
class DeparmentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ('name',)

@admin.register(UnitsOfMeasurement)
class UnitsOfMeasurementAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ('name',)

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'unit_of_measurement', 'is_active']
    list_filter = ('name', 'existence', 'brand', 'unit_of_measurement',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['legal_document', 'business_name']
    list_filter = ('legal_document', 'business_name',)
