
from django.db.models import Q
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from projects.models import Project, ProjectLink
from learning_rebellion.signals import site_tracker
from learning_rebellion.utils import get_page

def home_view(request):
    site_tracker.send(sender=None, request=request)
    
    project_page = get_page('projects')
    projects = Project.objects.filter(active=True).order_by('order')
    paginator = Paginator(projects, 5)
    
    try:
        page = int(request.GET. get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        podcasts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        projects = paginator.page(paginator.num_pages)
    
    return render(request, 'projects/home.html',
                          {'project_page': project_page,
                           'page': projects,
                           'projects_active': True})