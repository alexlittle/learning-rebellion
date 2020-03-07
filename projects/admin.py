from django.contrib import admin
from projects.models import Project, ProjectLink


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',  'order', 'active', 'slug')
    search_fields = ['title',  'body', 'slug']

    
class ProjectLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'active', 'slug')
    search_fields = ['title',  'body', 'slug']

    
admin.site.register(Project, ProjectAdmin) 
admin.site.register(ProjectLink, ProjectLinkAdmin) 