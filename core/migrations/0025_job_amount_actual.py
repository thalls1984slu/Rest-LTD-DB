# Generated by Django 5.0.1 on 2024-06-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_job_job_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='amount_actual',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]