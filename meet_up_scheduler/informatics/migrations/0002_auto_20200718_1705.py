# Generated by Django 3.0.3 on 2020-07-18 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='duration',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='seminar',
            name='time',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
    ]
