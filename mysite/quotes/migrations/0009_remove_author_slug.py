# Generated by Django 4.0 on 2022-01-04 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0008_author_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='slug',
        ),
    ]