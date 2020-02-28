
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',  'show_preview_url', 'slug', 'active')
    search_fields = ['title',  'body', 'slug']
    
    def show_preview_url(self,obj):
        return format_html("<a href="+reverse('blog_article', args={obj.slug}) + "?preview=1>"+ obj.title +" - preview</a>")
    
    show_preview_url.short_description = "Preview"
    
admin.site.register(Blog, BlogAdmin) 