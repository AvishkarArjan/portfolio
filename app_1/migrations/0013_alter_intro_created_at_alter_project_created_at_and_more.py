# Generated by Django 5.0.1 on 2024-01-07 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0012_remove_publication_authors_publication_main_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 18, 12, 45, 273566, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 18, 12, 45, 277089, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='researchinterest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 18, 12, 45, 274209, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='thingsimplanning',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 18, 12, 45, 274821, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='workex',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 18, 12, 45, 275504, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='workex',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 7, 18, 12, 45, 275441, tzinfo=datetime.timezone.utc)),
        ),
    ]
