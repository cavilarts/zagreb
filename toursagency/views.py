from django.shortcuts import render
from .models import Tour

def index(request):
    tours = Tour.objects.all()
    context = {'tours': tours}

    return render(request, 'index.html', context)
