# Generated by Django 4.2.3 on 2023-08-24 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrics2', '0016_site_fabrics'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabric',
            name='hasFull',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fabric',
            name='hasImage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='site',
            name='hasFull',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='site',
            name='hasImage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='site',
            name='fabrics',
            field=models.ManyToManyField(blank=True, related_name='sites', to='fabrics2.fabric'),
        ),
    ]
