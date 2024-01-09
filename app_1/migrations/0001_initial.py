# Generated by Django 5.0.1 on 2024-01-07 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=10000000)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 7, 6, 9, 50, 443785))),
                ('project_time', models.DateField(blank=True)),
                ('details', models.CharField(default='Technologies used: ', max_length=1000)),
                ('link_1', models.CharField(blank=True, max_length=100000)),
                ('link_2', models.CharField(blank=True, max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('title', models.CharField(max_length=10000)),
                ('authors', models.CharField(max_length=10000)),
                ('details', models.CharField(max_length=10000)),
                ('poster_link', models.CharField(blank=True, max_length=10000)),
                ('paper_link', models.CharField(blank=True, max_length=10000)),
                ('abstract_link', models.CharField(blank=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=10000000)),
            ],
        ),
        migrations.CreateModel(
            name='ThingsImPlanning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 7, 6, 9, 50, 441647))),
            ],
        ),
        migrations.CreateModel(
            name='WorkEx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=10000000)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 7, 6, 9, 50, 442294))),
                ('ps', models.CharField(blank=True, max_length=10000)),
                ('link_1', models.CharField(blank=True, max_length=100000)),
                ('link_2', models.CharField(blank=True, max_length=100000)),
            ],
        ),
    ]
