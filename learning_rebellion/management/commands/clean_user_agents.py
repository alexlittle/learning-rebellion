
"""
Management command to remove bots/crawlers from trackers
"""

from optparse import make_option

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from learning_rebellion.models import Tracker
from learning_rebellion.lib import search_crawler

class Command(BaseCommand):
    help = "Removes bots/crawlers from trackers"


    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        rts = Tracker.objects.all()
        for rt in rts:
            if search_crawler.is_search_crawler(rt.agent):
                print "found: " + rt.agent
                rt.delete()
             
            