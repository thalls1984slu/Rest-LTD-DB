# Generated by Django 5.0.1 on 2024-02-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_job_display_image_alter_picture_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='display_image',
            field=models.ImageField(blank=True, default='/media/job_images/rest_logo.jpg', null=True, upload_to='job_images/'),
        ),
    ]
