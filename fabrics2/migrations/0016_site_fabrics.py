# Generated by Django 4.2.3 on 2023-08-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrics2', '0015_alter_fabric_refs_alter_slide_refs'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='fabrics',
            field=models.ManyToManyField(blank=True, null=True, related_name='sites', to='fabrics2.fabric'),
        ),
    ]
