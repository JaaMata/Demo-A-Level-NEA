# Generated by Django 3.2.5 on 2021-08-14 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210814_2000'),
        ('Inventory', '0025_auto_20210814_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.shippingaddressmodel'),
        ),
    ]
