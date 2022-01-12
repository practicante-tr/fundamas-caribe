from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mass_mail, BadHeaderError
from .models import Post, Category, Comment, Subscription
from django.contrib.auth.models import User
from datetime import datetime, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.contrib import messages
import re
from config import settings
from .utils import *

# Create your views here.

def blog(request):
    blogs = Post.objects.order_by('-created_at').exclude(category=4)

    recent_posts = blogs[:4]

    #El siguiente QuerySet me trae todos los valores del modelo(tabla) Categoría y adicional a eso,
    #realiza un conteo de el número de Posts que tiene cada Categoría (annotate) esto me permite listarlas
    #en el template mediante una interacción de un bucle For.
    #Documentación
    #https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
    #https://stackoverflow.com/questions/53468286/how-to-count-blog-categories-in-django-and-display-them-in-a-template
    categories = Category.objects.annotate(posts_count=Count('post'))


    #Suscription implementation
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']

        #Validating input name before save into database
        name_validation = re.search('^[a-zA-Z_ñÑ ]+$', name)
        if name_validation:
            #Validating input email if exist in the database before save it
            if Subscription.objects.filter(email=email).exists():
                messages.warning(request, 'Ya te encuentras suscrito a nuestras noticias')
                return redirect('/blogs/')
            else:
                #if not exists, well im gona push it into database table
                subs = Subscription(name=name, email=email)

                #Starting sending Subscription's confirmation to Email

                #This tuple going to be send to users that just subscribe
                message_subs = ('¡Subscripcion exitosa! - Fundamas Caribe',
                                      f'Hola, '+name+'. Te damos la bienvenida a nuestra fundación, con esta subscripción totalmente gratis podrás estar al tanto de nuestras publicaiones',
                                      settings.EMAIL_HOST_USER,
                                      [email]
                )

                #Admin (superuser) information
                admin_info = User.objects.filter(is_superuser=True)
                admin_emails = []
                for i in admin_info:
                    admin_emails.append(i.email)

                #This tuple going to be send to admins are superuser
                message_admin = ('Un Nuevo Usuario se ha Suscrito',
                                 'El usuario '+name+' se ha suscrito a las noticias del blog',
                                 settings.EMAIL_HOST_USER,
                                 admin_emails
                )

                if message_admin and message_subs:
                    try:
                        send_mass_mail((message_subs, message_admin), fail_silently=False)
                    except BadHeaderError as e:
                        messages.error(request, 'Lo siento. Tuvimos inconvenientes en enviarte el correo de bienvenido.')
                        return redirect('/blogs/')

                save = subs.save()
                #After this, I gonna validate if the save() query goes successfully
                messages.success(request, '¡Muchas gracias! Que quieras estar atento a nuestro progreso nos emociona.')
                return redirect('/blogs/')
        else:
            messages.error(request, '¡Perdon! El Nombre que ingresaste contiene valores no permitidos')
            return redirect('/blogs/')


    #Number of pages will show in the template
    paginator = Paginator(blogs, 6)
    #Getting number of page.
    page_num = request.GET.get('page', 1)
    try:
        pages = paginator.get_page(page_num)
    except EmptyPage as e:
        #Send me until the end of the page number
        pages = paginator.get_page(page_num, 1)

    data ={
        'blogs': pages,
        'recent_posts': recent_posts,
        'categories': categories,
    }
    return render(request, 'blogs/blog.html', data)

def blogs_details(request, id):

    detail_blogs = get_object_or_404(Post,pk=id)
    recent_posts = Post.objects.order_by('-created_at')[:4]
    comments = detail_blogs.comments.filter(active=True).count() #Esta consulta recibe el id del methodo, este es utilizado por el query set para saber que Post es el que se esta tomando. Documentación https://djangocentral.com/building-a-blog-application-with-django/ https://djangocentral.com/creating-comments-system-with-django/
    list_comments = Comment.objects.filter(post__id=id, active=True).order_by('-created_on')
    categories = Category.objects.annotate(posts_count=Count('post'))

    data ={
        'detail_blogs': detail_blogs,
        'recent_posts': recent_posts,
        'comments': comments,
        'list_comments': list_comments,
        'categories': categories,
    }
    return render(request, 'blogs/blogs_details.html', data)

def posts_by_category(request, id):
    posts_categories = Post.objects.filter(category=id).order_by('-created_at')

    data = {
        'posts_categories': posts_categories,

    }
    return render(request, 'blogs/posts_category.html', data)

def comment(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        body    = request.POST['body']
        name    = request.POST['name']
        email   = request.POST['email']

        #Made this querysey cause the Comment model retrive a post id values that is not a number
        post = get_object_or_404(Post,pk=post_id)

        data = Comment(post=post, body=body, name=name, email=email)
        saved = data.save()

        messages.success(request, 'Tu comentario fue recibido y pronto sera aprobado')
        return redirect('/blogs/'+ post_id)

def subscription(request):
    
     
    if  request.method == 'POST':

        post_id = request.POST['post_id']
        name = request.POST['name']
        email = request.POST['email']

        nameValid = re.search('^[a-zA-Z_ñÑ ]+$', name)
        if nameValid:
            #This Email exists?
            if Subscription.objects.filter(email=email).exists(): #if not exists
                messages.warning(request, subscribed)
                return redirect('/blogs/'+post_id)
            else:
                #Saving the data
                data = Subscription(name=name, email=email)
                save = data.save()     

                #Getting the Admins' Emails
                admins = User.objects.filter(is_superuser=True)
                emails = [] #This will have Admis' Emails
                for admin in admins:
                    emails.append(admin.email) #Appending Emails

                #Building Emails body
                msg_subs = ('¡Subscripcion exitosa! - Fundamas Caribe',
                            message_subs,
                             settings.EMAIL_HOST_USER,
                             [email])

                msg_admin = ('Tenemos un nuevo subscriptor',
                            'El usuari@ '+name+' se ha subscrito a las noticias del blog, dale una cordial bienvenida'+ message_admin,
                            settings.EMAIL_HOST_USER,
                            emails)

                #Bodies are Okay?
                if msg_subs and msg_admin:
                    try:
                        #sending emails...
                        send_mass_mail((msg_subs, msg_admin), fail_silently=False)
                        
                    except Exception as e:
                        messages.error(request, error_try_msg)
                        return redirect('/blogs/'+post_id)
                else:
                    messages.error(request, error_msg)
                    return redirect('/blogs/'+post_id)

            #if everything is okay...    
            messages.success(request, success_msg)
            return redirect('/blogs/'+post_id)
        else:
            messages.error(request, error_name_msg)
            return redirect('/blogs/'+post_id)
        

