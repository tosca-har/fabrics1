# Generated by Django 4.2.3 on 2023-10-01 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pottery', '0005_report_remove_industry_time_industry_time_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='time',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
