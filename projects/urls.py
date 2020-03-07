from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from projects import views as projects_views

urlpatterns = [
    url(r'^$', projects_views.home_view, name="projects_home"),
    url(r'^(?P<slug>\w[\w/-]*)$', projects_views.project_view, name="projects_single"),
]