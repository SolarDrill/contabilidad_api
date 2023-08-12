# Generated by Django 4.2.3 on 2023-08-12 02:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contabilidad_dev", "0003_accountingentry"),
    ]

    operations = [
        migrations.RenameField(
            model_name="accountingentry",
            old_name="description",
            new_name="descripcion",
        ),
        migrations.RenameField(
            model_name="accountingentry",
            old_name="entry_date",
            new_name="fecha_registro",
        ),
        migrations.RemoveField(
            model_name="accountingentry",
            name="account",
        ),
        migrations.RemoveField(
            model_name="accountingentry",
            name="entry_amount",
        ),
        migrations.RemoveField(
            model_name="accountingentry",
            name="entry_identifier",
        ),
        migrations.RemoveField(
            model_name="accountingentry",
            name="inventory_type_identifier",
        ),
        migrations.RemoveField(
            model_name="accountingentry",
            name="movement_type",
        ),
        migrations.RemoveField(
            model_name="accountingentry",
            name="status",
        ),
        migrations.AddField(
            model_name="accountingentry",
            name="auxiliar",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="accountingentry",
            name="cuenta_contable",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="accountingentry",
            name="estado",
            field=models.CharField(default="R", max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="accountingentry",
            name="monto",
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="accountingentry",
            name="tipo_movimiento",
            field=models.CharField(choices=[("DB", "Debit"), ("CR", "Credit")], default="DB", max_length=2),
            preserve_default=False,
        ),
    ]
