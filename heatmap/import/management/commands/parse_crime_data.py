import requests
import json
import time
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Parses json from nyc database and outputs selected data to be fed into map'
    def handle(self, *args, **options):
    	#All 311 Service Requests from 2010 to present. This information is automatically updated daily
        crimes = requests.get("http://data.cityofnewyork.us/api/views/maj4-ux6k/rows.json")
        #time.sleep(.3)
        crimedata = json.loads(crimes.text)
        #All Columns
        format = crimedata['meta']['view']['columns']
        #Fields in each Column (loop through and get it): "id","name","dataTypeName","fieldName","position","renderTypeName","format"
        #Data for Columns (loop through each array to access comma seperated array with each position corresponding to column values)
        data = crimedata['data']
        
