import requests
import json
import time
class Command(BaseCommand):
    help = 'Parses json from nyc database and outputs selected data to be fed into map'
    def handle(self, *args, **options):
        latlngString = requests.get("http://data.cityofnewyork.us/api/views/maj4-ux6k/rows.json")
        #time.sleep(.3)
        crimes = json.loads(latlngString.text)
            
        data = crimes['data']
        format = crimes['meta']['format']
