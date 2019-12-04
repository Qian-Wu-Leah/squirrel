from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting

from django.forms import ModelForm

class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'

def map(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings':sightings,
            }
    return render(request,'squirrel_tracker/map.html',context)


def sightings(request):
<<<<<<< HEAD
    sightings = Sighting.objects.all()
    context = {
        'sightings':sightings, 
        }
=======
    squirrels = Sighting.objects.all()
    context = {
            'squirrels':squirrels,
            }
>>>>>>> bc6d3fd0572d70b8ecd44d4445ab31aac050092b
    return render(request,'squirrel_tracker/sightings.html',context)

def stats(request):
    return HttpResponse(f"STATS")

def add(request): 
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():           
            form.save()
            return redirect('sightings/')
    else:
        form = SightingForm()
    return render(request, 'squirrel_tracker/add.html', {'form': form})

def ID(request,squirrel_ID):
    squirrel = Sighting.objects.get(unique_squirrel_ID = squirrel_ID)
    context = {
            'squirrel':squirrel,
            }
    return render(request,'squirrel_tracker/ID.html',context)


