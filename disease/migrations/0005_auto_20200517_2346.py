# Generated by Django 3.0.6 on 2020-05-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0004_diseases_expected_recovery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseases',
            name='Expected_recovery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
