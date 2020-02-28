from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from learning_rebellion.fields import AutoSlugField

class Blog(models.Model):
    display_date = models.DateTimeField(default=timezone.now)
    title = models.TextField(blank=False)
    slug = AutoSlugField(populate_from='title', max_length=100, blank=True, null=True)
    body = RichTextField()
    image = models.FileField(upload_to="images", blank=True, default=None)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title