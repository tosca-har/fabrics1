# Generated by Django 4.2.3 on 2023-08-09 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabrics2', '0010_alter_slide_comments_alter_slide_desc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='comments',
        ),
    ]
