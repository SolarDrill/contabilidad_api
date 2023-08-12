from django import forms
from .validators import validate_dominican_legal_document
from .models import Deparments, UnitsOfMeasurement, Items, Supplier, AccountingEntry

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Deparments
        fields = ['name']

class UnitsOfMeasurementForm(forms.ModelForm):
    class Meta:
        model = UnitsOfMeasurement
        fields = ['name', 'description']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'description', 'existence', 'brand', 'unit_of_measurement']

class SupplierForm(forms.ModelForm):
    legal_document = forms.CharField(validators=[validate_dominican_legal_document])
    class Meta:
        model = Supplier
        fields = ['legal_document', 'business_name']

class AccountingEntryForm(forms.ModelForm):
    class Meta:
        model = AccountingEntry
        fields = ['auxiliar', 'descripcion', 'monto', 'cuentaDB', 'cuentaCR']
