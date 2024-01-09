from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    intros = Intro.objects.all()
    r_interests = ResearchInterest.objects.all()
    things_planning = ThingsImPlanning.objects.all()
    work_ex = WorkEx.objects.all()
    publications = Publication.objects.all()
    projects = Project.objects.all()

    content = {
        'intros': intros[0],
        'r_interests': r_interests[0],
        'things_planning': things_planning,
        'work_ex': work_ex,
        'publications': publications,
        'projects': projects
    }
    return render(request, 'index.html', {'content': content})
