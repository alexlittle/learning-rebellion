
from django.db.models import Q
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext

from learning_rebellion.models import Podcast, Tracker, Page
from blog.models import  Blog
from learning_rebellion.signals import site_tracker

def get_page(slug):
    try:
        page = Page.objects.get(slug='home',active=True)
    except Page.DoesNotExist:
        return None
    return page

def home_view(request):
    site_tracker.send(sender=None, request=request)
    podcasts = Podcast.objects.filter(active=True).order_by('-date_display')[:3]
    news = Blog.objects.filter(active=True).order_by('-display_date')[:3]
    
    return render(request, 'lr/home.html',
                          {'home_active': True,
                           'podcasts': podcasts,
                           'page': get_page('home'),
                           'news': news })
    
def podcast_view(request, podcast_slug):
    site_tracker.send(sender=None, request=request)
    preview = request.GET.get("preview", 0)
    if preview == "1":
        podcast = Podcast.objects.get(slug=podcast_slug)
    else:
        podcast = Podcast.objects.get(slug=podcast_slug, active=True)
    return render(request, 'podcast/podcast-full-post.html',
                          {'podcast': podcast,
                           'podcast_active': True})
