# Generated by Django 5.0.1 on 2024-01-07 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0009_project_tech_used_alter_intro_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workex',
            name='duration',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='intro',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 15, 31, 33, 170508, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 15, 31, 33, 175562, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='researchinterest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 15, 31, 33, 171291, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='thingsimplanning',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 15, 31, 33, 171896, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='workex',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 15, 31, 33, 172545, tzinfo=datetime.timezone.utc)),
        ),
    ]
