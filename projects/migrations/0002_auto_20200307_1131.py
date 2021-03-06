# Generated by Django 2.2.10 on 2020-03-07 11:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, default=None, upload_to='projects/images'),
        ),
        migrations.AlterField(
            model_name='projectlink',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='projectlink',
            name='image',
            field=models.FileField(blank=True, default=None, upload_to='projects/links/images'),
        ),
    ]
