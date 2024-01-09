from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


class Intro(models.Model):
    body_1 = models.CharField(max_length=100000, default="Add intro here")
    body_2 = models.CharField(max_length=100000, blank=True)
    body_3 = models.CharField(max_length=100000, blank=True)
    body_4 = models.CharField(max_length=100000, blank=True)
    created_at = models.DateTimeField(default=timezone.now())


class ResearchInterest(models.Model):
    body = models.CharField(max_length=10000000)
    created_at = models.DateTimeField(default=timezone.now())


class ThingsImPlanning(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    # created_at = models.DateTimeField(default = datetime.now(), blank=True)
    created_at = models.DateTimeField(default=timezone.now())


class WorkEx(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    body = models.CharField(max_length=10000000)
    end_date = models.DateField(default=timezone.now())
    duration = models.CharField(max_length=1000, blank=True)
    # created_at = models.DateTimeField(default = datetime.now(), blank=True)
    created_at = models.DateTimeField(default=timezone.now())
    ps = models.CharField(max_length=10000, blank=True)
    link_1 = models.CharField(max_length=100000, blank=True)
    link_2 = models.CharField(max_length=100000, blank=True)


class Publication(models.Model):
    year = models.DateField()
    title = models.CharField(max_length=10000)
    main_author = models.CharField(max_length=10000, blank=True)
    other_authors = models.CharField(max_length=10000, blank=True)
    details = models.CharField(max_length=10000)
    poster_link = models.CharField(max_length=10000, blank=True)
    paper_link = models.CharField(max_length=10000, blank=True)
    abstract_link = models.CharField(max_length=10000, blank=True)
    bibtex = models.CharField(max_length=10000, blank=True)


class Project(models.Model):
    title = models.CharField(max_length=100)
    # created_at = models.DateTimeField(default = datetime.now(), blank=True)
    created_at = models.DateTimeField(default=timezone.now())
    project_time = models.DateField(blank=True)
    details = models.CharField(max_length=100000, blank=True)
    tech_used = models.CharField(
        max_length=1000, default="Technologies used: ")
    link_1 = models.CharField(max_length=100000, blank=True)
    link_2 = models.CharField(max_length=100000, blank=True)
