from django.urls import path
from . import views
urlpatterns = [
    # path('blog', views.blog, name='blog'), NO TOCAR
    path('', views.blog, name='blog'),
    path('<int:id>', views.blogs_details, name='blogs_details'),
    path('posts/<int:id>', views.posts_by_category, name='posts_by_category'),
    path('comment', views.comment, name='comment'),
    path('subscription', views.subscription, name='subscription'),  
]
