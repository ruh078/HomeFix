# Generated by Django 3.2.6 on 2021-08-31 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_fix', '0005_auto_20210827_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_provider',
            name='id',
        ),
        migrations.AlterField(
            model_name='service_provider',
            name='service_id',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
