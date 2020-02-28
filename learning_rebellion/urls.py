from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
import blog
from learning_rebellion import views as lr_views

urlpatterns = [
    url(r'^$', lr_views.home_view, name="lr_home"),
    url(r'^news/', include('blog.urls')),
]