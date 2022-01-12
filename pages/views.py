from django.shortcuts import render, redirect
from .models import Contact, Team, Project
from blogs.models import Post
from django.contrib import messages
import re

#https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
#https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
#email_patron = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
email_patron = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")


# Create your views here.
def home(request):
    teams = Team.objects.all()
    blogs = Post.objects.order_by('-created_at').exclude(category=4) #Fetch all object from Post model and oradering by created date, only blogs dont  Projects
    
    data ={
        'teams': teams,
        'blogs': blogs,
        
    }
    return render(request,'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data ={
        'teams':teams,
    }
    return render(request, 'pages/about.html', data)

def projects(request):
    projects = Project.objects.order_by('-created_at')
    data = {
        'projects': projects,
    }
    return render(request, 'pages/projects.html', data)

def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        
        #Inputs validation
        if re.search('^[a-zA-Z_ñÑ ]+$', name):
            if re.fullmatch(email_patron, email):
                if re.search('^[a-zA-Z_ñÑ., ]+$', subject):
                    #Saving...
                    data = Contact(message=message,name=name, email=email, subject=subject)
                    
                    #send email
                    save = data.save()
                    messages.success(request, '¡Gracias! Pontro estaremos enviando respuesta a tu consulta')
                    return redirect('contact')                    
                else:
                    #When subject validation fails then
                    messages.error(request, '¡Perdon! El asunto que ingresaste contiene carácteres no permitidos')
                    return redirect('contact')
            else:
                #When email validation fails then
                messages.error(request, '¡Perdon! El correo que ingresaste contiene carácteres no permitidos')
                return redirect('contact')
        else:
            #When name validation fails then
            messages.error(request, '¡Perdon! El nombre que ingresaste contiene carácteres no permitidos')
            return redirect('contact')  
     
    return render(request,'pages/contact.html')
