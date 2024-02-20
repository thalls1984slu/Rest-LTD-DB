# Generated by Django 5.0.1 on 2024-02-19 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='barcode',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='brand',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='cost',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='location',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
    ]