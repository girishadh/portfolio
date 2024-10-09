from django.shortcuts import render
from .models import Projects, Skill

# Create your views here.
def home(request):
    projects = Projects.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'portfolioSite/home.html', context)