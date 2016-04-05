import json
import urllib2
from pprint import pprint

N = int(raw_input('Number of cities?\n'))
cities = []
for i in range(N):
    inp = raw_input()
    urlarg = inp.replace(' ','+')
    page = urllib2.urlopen('https://maps.googleapis.com/maps/api/directions/json?origin=IIT+Bombay&destination='+urlarg)
    resp = page.read()
    data = json.loads(resp)
    pprint(data['routes'][0]['legs'][0]['value'])
    #cities.append([s,a])
print cities


