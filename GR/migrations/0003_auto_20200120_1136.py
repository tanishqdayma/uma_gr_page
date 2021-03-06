# Generated by Django 2.2.9 on 2020-01-20 11:36

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('GR', '0002_auto_20200120_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grpage',
            name='content',
            field=wagtail.core.fields.StreamField([('Main', wagtail.core.blocks.StructBlock([('points', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('point', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('pdfs', wagtail.core.blocks.ListBlock(wagtail.documents.blocks.DocumentChooserBlock(required=True)))])))])), ('Related', wagtail.core.blocks.StructBlock([('points', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('point', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('pdfs', wagtail.core.blocks.ListBlock(wagtail.documents.blocks.DocumentChooserBlock(required=True)))])))]))], blank=True, null=True),
        ),
    ]
