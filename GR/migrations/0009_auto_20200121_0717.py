# Generated by Django 2.2.9 on 2020-01-21 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GR', '0008_auto_20200121_0713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grpage',
            old_name='content1',
            new_name='content',
        ),
    ]