# Generated by Django 5.0.1 on 2024-02-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_job_job_risk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='job_images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='images',
        ),
        migrations.AddField(
            model_name='job',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, related_name='job_img', to='core.picture'),
        ),
    ]
