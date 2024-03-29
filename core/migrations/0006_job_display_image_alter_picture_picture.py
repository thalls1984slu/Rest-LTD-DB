# Generated by Django 5.0.1 on 2024-02-18 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_document_remove_job_documents_alter_job_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='display_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_display_image', to='core.picture'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(blank=True, default='rest/img/rest_logo.jpg', null=True, upload_to='job_images/'),
        ),
    ]
