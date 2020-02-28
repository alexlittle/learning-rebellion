from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Page (models.Model):
    active = models.BooleanField(default=False)
    title = models.CharField(max_length=300, blank=False, null=False)
    menu_title = models.CharField(max_length=30, blank=False, null=False)
    slug = models.CharField(max_length=30, blank=False, null=False)
    template = models.CharField(max_length=30, blank=False, null=False)
    content = RichTextField(null=True, blank=True, default=None)
    
    def __str__(self):
        return self.title
    
    
class Podcast (models.Model):
    active = models.BooleanField(default=False)
    title = models.CharField(max_length=300, blank=False, null=False)
    date_display = models.DateTimeField('date', default=timezone.now)  
    description = models.TextField(blank=True, null=True, default=None)
    image = models.FileField(upload_to="projects",blank=True, default=None)
    podcast = models.FileField(upload_to="podcasts",blank=True, default=None)
    
    def __str__(self):
        return self.title
    
class Tracker (models.Model):
    tracker_date = models.DateTimeField('date tracked',default=timezone.now)
    ip = models.GenericIPAddressField()
    agent = models.TextField(blank=True)
    url = models.TextField(blank=True, null=True, default=None)
    
    def __str__(self):
        return self.ip