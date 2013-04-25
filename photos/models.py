from django.db import models


class Entry(models.Model):
    comment = models.CharField(max_length=100)
    photo = models.FileField(upload_to='photos')
