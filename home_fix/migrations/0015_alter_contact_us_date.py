# Generated by Django 3.2.6 on 2021-10-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_fix', '0014_alter_service_requested_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
