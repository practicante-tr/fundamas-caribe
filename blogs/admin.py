from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Post, Comment,Subscription

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    list_display_links = ('id','name')
    search_fields =  ('id','name')
    list_filter = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']


    # tenemos el método de acciones que nos ayudará a aprobar muchos objetos
    # de comentario a la vez, el approve_commentsmétodo es una función simple
    # que toma un conjunto de consultas y actualiza el campo booleano activo a True.
    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class PostAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40"  />'.format(object.photo.url))

    #Alias to the method
    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'title', 'category', 'autor', 'created_at')
    list_display_links = ('id', 'thumbnail', 'title', 'category','autor','created_at')
    search_fields = ('id', 'thumbnail', 'title', 'category',  'autor',  'created_at')
    list_filter =('category', 'autor', 'created_at')

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','subs_date')
    list_filter = ('name', 'email',  'subs_date')
    search_fields = ('name', 'email', 'subs_date')

admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
