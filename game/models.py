from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Puzzle(models.Model):
    photo = models.ImageField(upload_to='/puzzles/')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    submission_time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)

    def __unicode__(self):
        return self.creator + self.submission_time


class Answer(models.Model):
    photo = models.ImageField(upload_to='/answers/')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    submission_time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    puzzle = models.ForeignKey(Puzzle)
    is_correct = models.NullBooleanField()

    def __unicode__(self):
        return self.creator + self.submission_time
