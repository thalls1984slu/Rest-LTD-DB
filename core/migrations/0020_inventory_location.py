# Generated by Django 5.0.1 on 2024-02-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_inventory_options_inventory_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='location',
            field=models.CharField(default=0, max_length=255),
        ),
    ]