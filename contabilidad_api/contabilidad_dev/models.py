from django.db import models
from config.abstract_models import CommonInfo

class Deparments(CommonInfo):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name

class UnitsOfMeasurement(CommonInfo):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Unit of measurement'
        verbose_name_plural = 'Units of measurement'

    def __str__(self):
        return self.name

class Items(CommonInfo):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    existence = models.IntegerField(null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    unit_of_measurement = models.ForeignKey(UnitsOfMeasurement, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name

class Supplier(CommonInfo):
    legal_document = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.business_name

class AccountingEntry(models.Model):
    descripcion = models.TextField()
    auxiliar = models.IntegerField()
    monto = models.IntegerField()
    cuentaCR = models.IntegerField()
    cuentaDB = models.IntegerField()

    class Meta:
        verbose_name = 'Accounting entry'
        verbose_name_plural = 'Accounting entries'

    def __str__(self):
        return self.descripcion
