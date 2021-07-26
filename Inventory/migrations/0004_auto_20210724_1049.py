# Generated by Django 3.2.5 on 2021-07-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_alter_book_borrowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='barcode',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='coverImage',
            field=models.ImageField(null=True, upload_to='bookCovers'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]