# Generated by Django 5.0.1 on 2024-10-13 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_alter_job_payment_type'),
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yearlyschedule',
            name='amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='yearlyschedule',
            name='employees',
            field=models.ManyToManyField(blank=True, related_name='maintenance_jobs', to='core.employee'),
        ),
        migrations.AddField(
            model_name='yearlyschedule',
            name='next_schdeuled_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='yearlyschedule',
            name='completed_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='yearlyschedule',
            name='scheduled_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='yearlyschedule',
            name='year',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
