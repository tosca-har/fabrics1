# Generated by Django 4.2.3 on 2023-10-01 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pottery', '0006_industry_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industry',
            name='time',
        ),
    ]
