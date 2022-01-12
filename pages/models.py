from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100, blank=True, null=True)
    twitter_link = models.URLField(max_length=100, blank=True, null=True)
    instragam_link = models.URLField(max_length=100, blank=True, null=True)
    web_link = models.URLField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        db_table = 'teams'
        ordering = ['id']


class Contact(models.Model):
    message = models.TextField(verbose_name='Mensaje', blank=False, null=False)
    name = models.CharField(max_length=50, verbose_name='Nombre', blank=False, null=False)
    email = models.CharField(max_length=50, verbose_name='Correo', blank=False, null=False)
    subject = models.CharField(max_length=100, verbose_name='Asunto', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        db_table = 'contacts'
        ordering = ['-id']
        

class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    description = RichTextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    
    def __str__(self):
            return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        db_table = 'project'
        ordering = ['-id']