from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Sighting
from .forms import SightingForm
from django.db.models import Count,Sum


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
    form = SightingForm(request.POST or None, instance=squirrel)
    context = {
            'squirrel':squirrel,
            'form':form,
            }
    if form.is_valid():
        squirrel = form.save()
        squirrel.save()
        context = {
                'squirrel':squirrel,
                'form':form,
                }
    return render(request,'squirrel_tracker/ID.html',context)

def delete(request, squirrel_ID):
    squirrel = Sighting.objects.get(unique_squirrel_ID = squirrel_ID)
    if request.method == 'POST':
        squirrel.delete()
        return redirect('sightings')
    return render(request, 'squirrel_tracker/delete.html')


#def update(request, squirrel_ID):
#    squirrel = Sighting.objects.get(unique_squirrel_ID = squirrel_ID)
#    if request.method == 'POST':
#        form = SightingForm(request.POST)
#        context = {
#                'form':form,
#                }
#        if form.is_valid():
#            squirrel = form.save()
#            squirrel.save()
#            return redirect('sightings/%s'%squirrel_ID)
#    else:

