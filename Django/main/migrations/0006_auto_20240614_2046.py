# Generated by Django 3.2.25 on 2024-06-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20240614_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='image',
            field=models.ImageField(upload_to='app_images/'),
        ),
        migrations.AlterField(
            model_name='task',
            name='app_image',
            field=models.ImageField(blank=True, null=True, upload_to='task_app_images/'),
        ),
        migrations.AlterField(
            model_name='task',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='task_screenshots/'),
        ),
    ]
