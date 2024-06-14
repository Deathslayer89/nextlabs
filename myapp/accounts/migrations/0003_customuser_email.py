# Generated by Django 5.0.6 on 2024-06-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_remove_customuser_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
    ]
