from django.contrib import admin
from django.utils.html import format_html
from .models import  Team, Contact, Project

class ProjectAdmin(admin.ModelAdmin):
    
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40"  />'.format(object.photo.url))

    #Alias to the method
    thumbnail.short_description = 'Portada'

    list_display = ('id', 'thumbnail', 'title', 'created_at')
    list_display_links = ('id', 'thumbnail', 'title', 'created_at')
    search_fields = ('id', 'thumbnail', 'title', 'created_at')
    list_filter = ('title', 'created_at')
    
admin.site.register(Project, ProjectAdmin)


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))

    #Alias to the method
    thumbnail.short_description = 'Photo'

    list_display = ('id','thumbnail','first_name', 'last_name', 'designation', 'created_at')
    list_display_links = ('first_name','thumbnail', 'last_name', 'designation')
    search_fields =  ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)


class ContactAdmin(admin.ModelAdmin):

    list_display = ('id','name','email', 'subject', 'created_at')
    list_display_links = ('id','name','email', 'subject')
    search_fields =  ('email', 'subject', 'created_at')
    list_filter = ('created_at',)

admin.site.register(Contact, ContactAdmin)

