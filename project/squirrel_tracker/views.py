from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting


def map(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings':sightings,
            }
    return render(request,'squirrel_tracker/map.html',context)

def sightings(request):
    return render(request,'squirrel_tracker/sightings.html',context={'squirrels':Sighting.objects.all})

def stats(request):
    return HttpResponse(f"STATS")

def add(request):
    return HttpResponse(f"ADD")

def ID(request,squirrel_ID):
    squirrel = Sighting.objects.get(unique_squirrel_ID = squirrel_ID)
    return HttpResponse(f"Hi, I'm pet {squirrel.unique_squirrel_ID}")



