from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Social_networks, Skill_Categories, Skills, Projects
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

    return render(request, 'index.html', infos)