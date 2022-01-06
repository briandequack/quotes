# Generated by Django 4.0 on 2022-01-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0014_author_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
