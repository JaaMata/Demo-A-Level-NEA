# Generated by Django 3.2.5 on 2021-08-10 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0016_auto_20210810_0409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='shipping_address',
        ),
    ]
