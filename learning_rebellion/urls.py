from django.conf.urls import url, include
from django.contrib import admin

from learning_rebellion import views as lr_views

urlpatterns = [
   url(r'^$', lr_views.home_view, name="lr_home"),
]