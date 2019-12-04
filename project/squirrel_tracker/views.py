from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Sighting
from .forms import SightingForm


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

