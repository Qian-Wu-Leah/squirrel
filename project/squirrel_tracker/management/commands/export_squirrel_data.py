from django.core.management.base import BaseCommand, CommandError
from squirrel_tracker.models import Sighting
import csv
import sys

class Command(BaseCommand):
    help = ("Output Sightings as csv")
   

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        from django.db.models import get_model
        squirrel_tracker, Sighting = 



    
