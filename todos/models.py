# coding: utf-8
from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    closed = models.BooleanField()
