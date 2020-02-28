# Generated by Django 2.2.10 on 2020-02-28 08:10

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=300)),
                ('menu_title', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=30)),
                ('template', models.CharField(max_length=30)),
                ('content', ckeditor.fields.RichTextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=300)),
                ('date_display', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('image', models.FileField(blank=True, default=None, upload_to='projects')),
                ('podcast', models.FileField(blank=True, default=None, upload_to='podcasts')),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracker_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date tracked')),
                ('ip', models.GenericIPAddressField()),
                ('agent', models.TextField(blank=True)),
                ('url', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
