# Generated by Django 5.0.1 on 2024-10-13 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_remove_employee_current_employee_employee_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='lease',
        ),
        migrations.AddField(
            model_name='job',
            name='payment_type',
            field=models.CharField(choices=[('PY', 'Payment'), ('LS', 'Lease')], default='PY', max_length=2),
        ),
    ]
