import csv
import datetime

from squirrel_tracker.models import Sighting

from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        
        def cleanBool(x):
            if x.lower() == 'true':
                return 'True'
            else:
                return 'False'

        with open(path,'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Unique Squirrel ID'] in Sighting.objects.values_list('unique_squirrel_ID', flat=True):
                    row['Unique Squirrel ID'] += '-R'

                s = Sighting(latitude = float(row['Y']),
                longitude = float(row['X']),
                unique_squirrel_ID = row['Unique Squirrel ID'],
                shift = row['Shift'],
                date = datetime.datetime.strptime(row['Date'],'%m%d%Y'),
                age = row['Age'].capitalize(),
                primary_fur_color = row['Primary Fur Color'].capitalize(),
                location = row['Location'].capitalize(),
                specific_location = row['Specific Location'].capitalize(),
                running = cleanBool(row['Running'].capitalize()),
                chasing = cleanBool(row['Chasing'].capitalize()),
                climbing = cleanBool(row['Climbing'].capitalize()),
                eating = cleanBool(row['Eating'].capitalize()),
                foraging = cleanBool(row['Foraging'].capitalize()),
                other_activities = row['Other Activities'].capitalize(),
                kuks = cleanBool(row['Kuks'].capitalize()),
                quaas = cleanBool(row['Quaas'].capitalize()),
                moans = cleanBool(row['Moans'].capitalize()),
                tail_flags = cleanBool(row['Tail flags'].capitalize()),
                tail_twitches = cleanBool(row['Tail twitches'].capitalize()),
                approaches = cleanBool(row['Approaches'].capitalize()),
                indifferent = cleanBool(row['Indifferent'].capitalize()),
                runs_from = cleanBool(row['Runs from'].capitalize()),
                )

                s.save()
