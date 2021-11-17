# Generated by Django 3.2.6 on 2021-08-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=3)),
                ('service', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('speciality', models.CharField(max_length=70)),
                ('min_charges', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('max_no_services', models.IntegerField()),
                ('assigned_no_services', models.IntegerField()),
            ],
        ),
    ]
