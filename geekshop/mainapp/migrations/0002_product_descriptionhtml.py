# Generated by Django 2.2 on 2019-04-29 11:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='descriptionHTML',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='описание продукта'),
        ),
    ]
