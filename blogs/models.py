from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Entry(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200, blank=False)
    contents = models.TextField(blank=False)
    pub_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
