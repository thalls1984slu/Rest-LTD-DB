# Generated by Django 5.0.3 on 2024-03-25 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('battery_brand', models.BooleanField(default=False)),
                ('inverter_brand', models.BooleanField(default=False)),
                ('panel_brand', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_status', models.CharField(choices=[('NW', 'New'), ('UD', 'Used')], default='NW', max_length=2)),
                ('model', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('size', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('serial', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='battery_brands', to='inventory.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Inverter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_status', models.CharField(choices=[('NW', 'New'), ('UD', 'Used')], default='NW', max_length=2)),
                ('grid_type', models.CharField(choices=[('NG', 'On Grid'), ('OG', 'Off Grid')], default='NG', max_length=2)),
                ('model', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('size', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('serial', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inverter_brands', to='inventory.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_status', models.CharField(choices=[('NW', 'New'), ('UD', 'Used')], default='NW', max_length=2)),
                ('model', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('size', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('serial', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panel_brands', to='inventory.brand')),
            ],
        ),
    ]
