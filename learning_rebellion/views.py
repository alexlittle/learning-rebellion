from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from learning_rebellion.signals import site_tracker
from learning_rebellion.models import Blog, Podcast

def home_view(request):
    site_tracker.send(sender=None, request=request)
    
    news = Blog.objects.all().order_by('-display_date')[:5]
    podcasts = Podcast.objects.all().order_by('-display_date')[:5]
    return render(request, 'lr/home.html',
                  {'news': news,
                   'podcasts': podcasts})