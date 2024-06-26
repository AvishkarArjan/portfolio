# Generated by Django 5.0.1 on 2024-01-07 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0007_alter_intro_created_at_alter_project_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 8, 36, 12, 976119, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 8, 36, 12, 999084, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='researchinterest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 8, 36, 12, 977012, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='thingsimplanning',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 8, 36, 12, 977653, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='workex',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 8, 36, 12, 978291, tzinfo=datetime.timezone.utc)),
        ),
    ]
