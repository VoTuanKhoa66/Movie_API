# Generated by Django 5.0.6 on 2024-06-13 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0003_alter_movie_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='parent_id',
        ),
    ]
