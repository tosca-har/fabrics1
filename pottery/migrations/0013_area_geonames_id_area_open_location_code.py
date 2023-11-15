# Generated by Django 4.2.3 on 2023-11-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pottery', '0012_alter_industry_language_family_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='geonames_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='open_location_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
