# Generated by Django 5.0 on 2024-04-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0011_lectures_publish_lectures_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectures',
            name='lecture',
            field=models.FileField(blank=True, null=True, upload_to='static/videos/'),
        ),
    ]
