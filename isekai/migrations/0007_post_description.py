# Generated by Django 5.0.4 on 2024-05-28 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isekai', '0006_favorite_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=datetime.datetime(2024, 5, 28, 14, 52, 52, 315421, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
    ]
