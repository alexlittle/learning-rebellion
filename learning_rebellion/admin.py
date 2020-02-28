from django.contrib import admin

from learning_rebellion.models import Podcast, Tracker, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title',  'menu_title', 'slug', 'active')
    search_fields = ['title',  'menu_title', 'slug', 'content']
 
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_display')     
    
class TrackerAdmin(admin.ModelAdmin):
    list_display = ('tracker_date', 'ip', 'url', 'agent') 
    


admin.site.register(Page, PageAdmin)      
admin.site.register(Podcast, PodcastAdmin) 
admin.site.register(Tracker, TrackerAdmin)  

