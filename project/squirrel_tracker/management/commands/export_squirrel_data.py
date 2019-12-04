from django.core.management.base import BaseCommand, CommandError
from squirrel_tracker.models import Sighting
from django.http import HttpResponse

import csv
import sys

class Command(BaseCommand):
    help = ("Output Sightings as csv")

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        field_names = [f.name for f in Sighting._meta.fields]

        with open(path, 'w') as csvf:
            writer = csv.writer(csvf)
            writer.writerow(field_names)
            for instance in Sighting.objects.all():
                writer.writerow([getattr(instance, f) for f in field_names])

