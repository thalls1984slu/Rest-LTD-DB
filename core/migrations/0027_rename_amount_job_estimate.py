# Generated by Django 5.0.1 on 2024-07-25 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_job_actual_end_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='amount',
            new_name='estimate',
        ),
    ]
