# Generated by Django 5.0.1 on 2024-01-20 22:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('wage', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('type',),
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cost', models.IntegerField(default=0)),
                ('size', models.IntegerField(default=0)),
                ('instock', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('job_progress', models.CharField(choices=[('CS', 'Consultation'), ('IP', 'In progress'), ('CL', 'Closed')], default='CS', max_length=2)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('duration', models.FloatField(default=0)),
                ('documents', models.FileField(blank=True, null=True, upload_to='job_documents/')),
                ('images', models.ImageField(blank=True, null=True, upload_to='job_images/')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='clients.client')),
                ('employees', models.ManyToManyField(related_name='jobs', to='core.employee')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.community')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.payment')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.system')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daysWorked', models.DecimalField(decimal_places=2, max_digits=5)),
                ('compensation', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.job')),
            ],
            options={
                'ordering': ('job',),
            },
        ),
    ]
