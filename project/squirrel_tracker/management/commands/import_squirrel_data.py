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

                s = Sighting(latitude = float(row['X']),
                longitude = float(row['Y']),
                unique_squirrel_ID = row['Unique Squirrel ID'],
                shift = row['Shift'],
                date = datetime.datetime.strptime(row['Date'],'%m%d%Y'),
                age = row['Age'],
                primary_fur_color = row['Primary Fur Color'],
                location = row['Location'],
                specific_location = row['Specific Location'],
                running = cleanBool(row['Running']),
                chasing = cleanBool(row['Chasing']),
                climbing = cleanBool(row['Climbing']),
                eating = cleanBool(row['Eating']),
                foraging = cleanBool(row['Foraging']),
                other_activities = row['Other Activities'],
                kuks = cleanBool(row['Kuks']),
                quaas = cleanBool(row['Quaas']),
                moans = cleanBool(row['Moans']),
                tail_flags = cleanBool(row['Tail flags']),
                tail_twitches = cleanBool(row['Tail twitches']),
                approaches = cleanBool(row['Approaches']),
                indifferent = cleanBool(row['Indifferent']),
                runs_from = cleanBool(row['Runs from']),
                )

                s.save()
