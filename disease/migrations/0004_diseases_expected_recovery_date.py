# Generated by Django 3.0.6 on 2020-05-17 18:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0003_auto_20200517_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseases',
            name='Expected_recovery_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 17, 18, 14, 51, 646668, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
