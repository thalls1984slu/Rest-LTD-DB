# Generated by Django 5.0.3 on 2024-04-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_battery_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='inverter',
            name='assigned',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='panel',
            name='assigned',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
