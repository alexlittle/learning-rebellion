# signals.py

from django.dispatch import Signal

from learning_rebellion.lib import search_crawler
from learning_rebellion.models import Tracker


site_tracker = Signal(providing_args=["request", "data"])


def site_tracker_callback(sender, **kwargs):
    request = kwargs.get('request')
    data = kwargs.get('data')
    
    ip = request.META.get('REMOTE_ADDR','0.0.0.0')
    agent = request.META.get('HTTP_USER_AGENT','unknown')
    
    if search_crawler.is_search_crawler(agent):
        return
    
    t = Tracker()
    t.url = request.build_absolute_uri()
    t.ip = ip
    t.agent = agent 
    t.save()
    
    return


site_tracker.connect(site_tracker_callback)