# Generated by Django 5.0.1 on 2024-08-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_rename_maintenane_type_job_maintenance_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]