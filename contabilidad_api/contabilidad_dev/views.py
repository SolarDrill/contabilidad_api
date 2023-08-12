from django.shortcuts import render, redirect, get_object_or_404
import json
from .models import Deparments, UnitsOfMeasurement, Items, Supplier, AccountingEntry
from .forms import DepartmentForm, UnitsOfMeasurementForm, ItemForm, SupplierForm, AccountingEntryForm
import requests

def main_page(request):
    return render(request, 'contabilidad/main.html')

def department_list(request):
    departments = Deparments.objects.all()
    return render(request, 'contabilidad/departments.html', {'departments': departments})

def unit_list(request):
    units = UnitsOfMeasurement.objects.all()
    return render(request, 'contabilidad/units.html', {'units': units})

def item_list(request):
    items = Items.objects.all()
    return render(request, 'contabilidad/items.html', {'items': items})

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'contabilidad/suppliers.html', {'suppliers': suppliers})

# Department CRUD

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = ItemForm()
    return render(request, 'contabilidad/department_create.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Deparments, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'contabilidad/department_update.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Deparments, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'contabilidad/department_delete.html', {'department': department})

# Items CRUD

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'contabilidad/item_create.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Items, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'contabilidad/item_update.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Items, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'contabilidad/item_delete.html', {'item': item})

# Unit CRUD

def unit_create(request):
    if request.method == 'POST':
        form = UnitsOfMeasurementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    else:
        form = UnitsOfMeasurementForm()
    return render(request, 'contabilidad/unit_create.html', {'form': form})

def unit_update(request, pk):
    unit = get_object_or_404(UnitsOfMeasurement, pk=pk)
    if request.method == 'POST':
        form = UnitsOfMeasurementForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    else:
        form = UnitsOfMeasurementForm(instance=unit)
    return render(request, 'contabilidad/unit_update.html', {'form': form})

def unit_delete(request, pk):
    unit = get_object_or_404(UnitsOfMeasurement, pk=pk)
    if request.method == 'POST':
        unit.delete()
        return redirect('unit_list')
    return render(request, 'contabilidad/unit_delete.html', {'unit': unit})

# Suppliers CRUD

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'contabilidad/supplier_create.html', {'form': form})

def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'contabilidad/supplier_update.html', {'form': form})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'contabilidad/supplier_delete.html', {'supplier': supplier})

def send_accounting_data(request):
    if request.method == 'POST':
        form = AccountingEntryForm(request.POST)
        if form.is_valid():
            instance_dict = {
                "descripcion": form.cleaned_data['descripcion'],
                "auxiliar": form.cleaned_data['auxiliar'],
                "cuentaDB": form.cleaned_data['cuentaDB'],
                "cuentaCR": form.cleaned_data['cuentaCR'],
                "monto": form.cleaned_data['monto'],
            }

            instance_json = json.dumps(instance_dict)

            response = requests.post('http://129.80.203.120:5000/post-accounting-entries', data=instance_json, headers={'Content-Type': 'application/json'})

            if response.status_code == 200:
                return render(request, 'success.html')
            else:
                return render(request, 'error.html')
    else:
        form = AccountingEntryForm()

    return render(request, 'contabilidad/post.html', {'form': form})
