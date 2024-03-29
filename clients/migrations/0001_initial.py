# Generated by Django 5.0.1 on 2024-01-20 22:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Communities',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_email', models.CharField(default=0, max_length=255)),
                ('contact_phone', models.CharField(default=0, max_length=255)),
                ('billing_address', models.CharField(default=0, max_length=255)),
                ('client_status', models.CharField(choices=[('NW', 'New'), ('RC', 'Recurrent'), ('RF', 'Referral')], default='NW', max_length=2)),
                ('accountType', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='clients.account')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.community')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='community',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.district'),
        ),
    ]
