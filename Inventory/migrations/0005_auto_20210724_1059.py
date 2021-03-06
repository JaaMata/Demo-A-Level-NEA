# Generated by Django 3.2.5 on 2021-07-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_auto_20210724_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='no', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='barcode',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='book',
            name='borrowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='coverImage',
            field=models.ImageField(upload_to='bookCovers'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
