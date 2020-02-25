from django.contrib import admin

from learning_rebellion.models import Blog, Podcast, Tracker

class BlogAdmin(admin.ModelAdmin):
    list_display = ('display_date', 'title',  'body', 'slug')
    search_fields = ['title',  'body', 'slug']
  
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('display_date', 'title',  'body', 'slug')
    search_fields = ['title',  'body', 'slug']  

class TrackerAdmin(admin.ModelAdmin):
    list_display = ('tracker_date', 'ip', 'url', 'agent')
    
admin.site.register(Blog, BlogAdmin)      
admin.site.register(Podcast, PodcastAdmin) 
admin.site.register(Tracker, TrackerAdmin)