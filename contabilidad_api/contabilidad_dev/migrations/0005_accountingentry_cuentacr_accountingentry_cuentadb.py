# Generated by Django 4.2.3 on 2023-08-12 02:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contabilidad_dev", "0004_rename_description_accountingentry_descripcion_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="accountingentry",
            name="cuentaCR",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="accountingentry",
            name="cuentaDB",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
