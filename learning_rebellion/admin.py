from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from learning_rebellion.models import Podcast, Tracker, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title',  'menu_title', 'slug', 'active')
    search_fields = ['title',  'menu_title', 'slug', 'content']
 
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_preview_url', 'date_display', 'active')  
    search_fields = ['title',  'body', 'slug']
       
    def show_preview_url(self,obj):
        return format_html("<a href="+reverse('podcast_article', args={obj.slug}) + "?preview=1>"+ obj.title +" - preview</a>")
    
    show_preview_url.short_description = "Preview"
    
class TrackerAdmin(admin.ModelAdmin):
    list_display = ('tracker_date', 'ip', 'url', 'agent') 
    


admin.site.register(Page, PageAdmin)      
admin.site.register(Podcast, PodcastAdmin) 
admin.site.register(Tracker, TrackerAdmin)  

