# Generated by Django 3.0.7 on 2020-06-09 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0013_auto_20200608_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
    ]
