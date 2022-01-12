from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from pages.models import Team
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Fecha de Creacion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categories'
        ordering = ['id']

class Post(models.Model):
    autor = models.ForeignKey(Team, on_delete=models.CASCADE)
    #comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='blogs/%Y/%m/%d/')
    title = models.CharField(max_length=150, verbose_name='Title')
    description = RichTextField()
    facebook_link = models.URLField(max_length=100, blank=True, null=True)
    twitter_link = models.URLField(max_length=100, blank=True, null=True)
    instragam_link = models.URLField(max_length=100, blank=True, null=True)
    web_link = models.URLField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'
        ordering = ['-id']

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comments'
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Subscription(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(max_length=50, verbose_name='Email')
    subs_date = models.DateTimeField(blank=True, default=datetime.now, verbose_name='Date of Subscription')

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        db_table = 'subscriptions'
        ordering = ['id']

    def __str__(self):
        return 'Subscription {}, Email {} by {}'.format(self.id,self.email, self.name)
