from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Import data from 2018 census'

    def add_argument(self,parser):
        parser.add_argument('path', help='Path to csv')

    def handle(self, *args, **kwargs):
        
