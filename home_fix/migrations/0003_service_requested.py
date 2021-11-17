# Generated by Django 3.2.6 on 2021-08-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_fix', '0002_alter_service_provider_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_requested',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_contact_no', models.CharField(max_length=12)),
                ('service_required', models.CharField(max_length=20)),
                ('area_in', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('requirement', models.CharField(max_length=150)),
                ('service_id', models.CharField(max_length=3)),
                ('date', models.DateField(auto_now=True)),
                ('rated', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
