# Generated by Django 3.2.5 on 2021-07-21 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='visible',
            new_name='borrowed',
        ),
        migrations.RemoveField(
            model_name='book',
            name='stock',
        ),
    ]
