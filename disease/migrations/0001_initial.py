# Generated by Django 3.0.6 on 2020-05-17 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('disease', models.CharField(max_length=30)),
                ('symptoms', models.CharField(max_length=200)),
                ('people_affected', models.IntegerField()),
                ('people_recovered', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=50)),
                ('symptoms', models.CharField(max_length=199)),
                ('recoveryperiod', models.CharField(blank=True, max_length=20)),
                ('medications', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('CaseDate', models.DateField(auto_now=True)),
                ('Expected_recovery_date', models.DateTimeField(blank=True)),
                ('threat_level', models.CharField(choices=[('HI', 'Highly Infectious'), ('I', 'Infectious'), ('Nc', 'Not Communicable')], max_length=20)),
            ],
        ),
    ]
