# Generated by Django 5.0.1 on 2024-01-09 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0013_alter_intro_created_at_alter_project_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 12, 39, 56, 748811, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 12, 39, 56, 749901, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='researchinterest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 12, 39, 56, 748811, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='thingsimplanning',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 12, 39, 56, 748811, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='workex',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 12, 39, 56, 748811, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='workex',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 9, 12, 39, 56, 748811, tzinfo=datetime.timezone.utc)),
        ),
    ]
