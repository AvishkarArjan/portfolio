# Generated by Django 5.0.1 on 2024-01-07 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='thingsimplanning',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='workex',
            name='created_at',
        ),
    ]
