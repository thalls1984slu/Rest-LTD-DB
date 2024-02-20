# Generated by Django 5.0.1 on 2024-02-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_inventory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'ordering': ('stock_type',)},
        ),
        migrations.AddField(
            model_name='inventory',
            name='brand',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='inventory',
            name='cost',
            field=models.CharField(default=0, max_length=255),
        ),
    ]