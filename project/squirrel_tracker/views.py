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
    squirrels = Sighting.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'squirrel_tracker/sightings.html',context)

def stats(request):
    return HttpResponse(f"STATS")

def add(request):
    return HttpResponse(f"ADD")

def ID(request,squirrel_ID):
    squirrel = Sighting.objects.get(unique_squirrel_ID = squirrel_ID)
    context = {
            'squirrel':squirrel,
            }
    return render(request,'squirrel_tracker/ID.html',context)


