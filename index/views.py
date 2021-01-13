from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import About, Social_networks, Skill_Categories, Skills, Projects

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
# Create your views here.
def index(request):

    about = About.objects.all()
    about = about[0]

    links = Social_networks.objects.all()

    skill_categories = Skill_Categories.objects.all()
    skills = Skills.objects.all()

    projects = Projects.objects.all()


    infos = {
        'about' : about, 
        'links' : links,
        'skill_categories' : skill_categories,
        'skills' : skills,
        'projects' : projects
        }


    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        

        try:
            send_mail(name, text, settings.EMAIL_HOST_USER, [email])
        except BadHeaderError:
            return HttpResponse('Invalid Header Found')
        return redirect('/')

    

    return render(request, 'index.html', infos)