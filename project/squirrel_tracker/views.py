from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Sighting

from django.forms import ModelForm
from django.db.models import Count, Sum

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
    squirrels = Sighting.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'squirrel_tracker/sightings.html',context)

def stats(request):
    count_age = Sighting.objects.values('age').order_by('age').annotate(age_count=Count('age'))
    count_running = Sighting.objects.values('running').order_by('running').annotate(running_count=Count('running'))
    count_chasing = Sighting.objects.values('chasing').order_by('chasing').annotate(chasing_count=Count('chasing'))
    count_primary_fur_color = Sighting.objects.values('primary_fur_color').order_by(
            'primary_fur_color').annotate(primary_fur_color_count=Count('primary_fur_color'))
    count_location = Sighting.objects.values('location').order_by(
            'location').annotate(location_count=Count('primary_fur_color'))
    
    context={
            'count_age':count_age,
            'count_running':count_running,
            'count_chasing':count_chasing,
            'count_primary_fur_color':count_primary_fur_color,
            'count_location':count_location,
            }
    return render(request, 'squirrel_tracker/stats.html', context)

def add(request): 
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():           
            form.save()
            return redirect('sightings')
    else:
        form = SightingForm()
    return render(request, 'squirrel_tracker/add.html', {'form': form})

def ID(request,squirrel_ID):
    squirrel = Sighting.objects.get(unique_squirrel_ID = squirrel_ID)
    context = {
            'squirrel':squirrel,
            }
    return render(request,'squirrel_tracker/ID.html',context)


