import requests
import json
import time
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Parses json from nyc database and outputs selected data to be fed into map'
    def handle(self, *args, **options):
        crimes = requests.get("http://data.cityofnewyork.us/api/views/maj4-ux6k/rows.json")
        #time.sleep(.3)
        crimedata = json.loads(crimes.text)
            
        data = crimedata['data']
        format = crimedata['meta']['format']
