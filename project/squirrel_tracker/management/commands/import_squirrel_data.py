from django.core.management.base import BaseCommand, CommandError

import requests

class Command(BaseCommand):
    help = 'Import data from 2018 census'

    def add_argument(self, parser):
        parser.add_argument('path', help='Path to save csv') 

    def handle(self, *args, **kwargs):
        url = 'https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv'
        response = requests.get(url)
        imported = response.content.decode('utf-8')
        self.stdout.write(imported)
