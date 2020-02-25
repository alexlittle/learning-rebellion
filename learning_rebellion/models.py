from django.db import models
from django.utils import timezone

class Blog(models.Model):
    display_date = models.DateTimeField('date tracked', default=timezone.now)
    title = models.TextField(blank=False)
    slug = models.CharField(max_length=30, blank=False, null=False)
    body = models.TextField(blank=False)
    image = models.FileField(upload_to="images", blank=True, default=None)

class Podcast(models.Model):
    display_date = models.DateTimeField('date tracked', default=timezone.now)
    title = models.TextField(blank=False)
    slug = models.CharField(max_length=30, blank=False, null=False)
    body = models.TextField(blank=False)
    image = models.FileField(upload_to="images", blank=True, default=None)
    file = models.FileField(upload_to="podcast", blank=True, default=None)
    
    
class Tracker (models.Model):
    tracker_date = models.DateTimeField('date tracked', default=timezone.now)
    ip = models.GenericIPAddressField()
    agent = models.TextField(blank=True)
    url = models.TextField(blank=True, null=True, default=None)
    
    def __str__(self):
        return self.ip