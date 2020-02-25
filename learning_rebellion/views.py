from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from learning_rebellion.signals import site_tracker


def home_view(request):
    site_tracker.send(sender=None, request=request)
    return render(request, 'lr/home.html')