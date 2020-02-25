from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _



def home_view(request):
    #projects = Project.objects.filter(active=True).order_by('order_by')
    
    return render(request, 'lr/home.html')