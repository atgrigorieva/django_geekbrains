# Generated by Django 2.2 on 2019-04-30 09:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20190429_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='описание'),
        ),
    ]
