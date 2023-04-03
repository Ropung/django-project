# Generated by Django 4.1.7 on 2023-04-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0005_reply"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="attached_file",
            field=models.FileField(null=True, upload_to="order/%Y-%m-%d/"),
        ),
        migrations.AddField(
            model_name="order",
            name="original_file_name",
            field=models.CharField(max_length=270, null=True),
        ),
    ]
