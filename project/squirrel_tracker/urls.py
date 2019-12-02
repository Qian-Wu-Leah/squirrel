from django.urls import path
from . import views

urlpatterns = [
        path('map/', views.map,name='map'),
        path('sightings/',views.sightings,name='sightings'),
        path('sightings/add/',views.add,name='add'),
        path('sightings/stats/',views.stats,name='stats'),
        path('sightings/<squirrel_ID>/',views.ID,name ='ID'),
        ]
