from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from learning_rebellion.fields import AutoSlugField


class Project(models.Model):
    create_date = models.DateTimeField(default=timezone.now)
    title = models.TextField(blank=False)
    slug = AutoSlugField(populate_from='title', max_length=100, blank=True, null=True)
    body = RichTextField()
    image = models.FileField(upload_to="projects/images", blank=True, default=None)
    active = models.BooleanField(default=False)
    order = models.IntegerField(default=0, null=False)
    
    def __str__(self):
        return self.title
    
    def get_links(self):
        return ProjectLink.objects.filter(project=self, active=True).order_by('order')
    
class ProjectLink(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)
    title = models.TextField(blank=False)
    slug = AutoSlugField(populate_from='title', max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, default=None)
    image = models.FileField(upload_to="projects/links/images", blank=True, default=None)
    active = models.BooleanField(default=False)
    order = models.IntegerField(default=0, null=False)
    url = models.TextField(blank=False)

    def __str__(self):
        return self.title