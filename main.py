import json
import urllib2
import math
f = math.pi/180
Rearth=6371000
page = urllib2.urlopen('https://maps.googleapis.com/maps/api/directions/json?origin=IIT+Bombay&destination=IIT+Bombay')
resp = page.read()
data = json.loads(resp)
ilat = (data['routes'][0]['legs'][0]['start_location']['lat'])*f
ilng = (data['routes'][0]['legs'][0]['start_location']['lng'])*f
class city:
    def __init__(self, s, d, lt, lg):
        self.name = s
        self.dist = d
        if lt == 100 or lg == 100:
            self.bldist = 'infi'
        else:
            phi = lt*f
            dl = lg*f - ilng
            y = math.sqrt( math.pow( math.cos(phi)*math.sin(dl), 2 ) + math.pow( math.cos(ilat)*math.sin(phi)-math.cos(phi)*math.sin(ilat)*math.cos(dl), 2 ))
            x = math.sin(phi)*math.sin(ilat)+math.cos(dl)*math.cos(phi)*math.cos(ilat)
            self.bldist = Rearth*math.atan2(y,x)
cities = []
with open('input.txt') as inpfile:
    N = int(inpfile.readline())
    for i in range(N):
        inp = inpfile.readline().strip('\n')
        urlarg = inp.replace(' ','+')
        page = urllib2.urlopen('https://maps.googleapis.com/maps/api/directions/json?origin=IIT+Bombay&destination='+urlarg)
        page2 = urllib2.urlopen('https://maps.googleapis.com/maps/api/directions/json?origin='+urlarg+'&destination='+urlarg)
        data = json.loads(page.read())
        data2 = json.loads(page2.read())
        try:
            dist = data['routes'][0]['legs'][0]['distance']['value']
        except IndexError:
            dist = 'infi'
        try:
            lat =data2['routes'][0]['legs'][0]['end_location']['lat']
            lng =data2['routes'][0]['legs'][0]['end_location']['lng']
        except IndexError:
            lat = 100
            lng = 100
        cities.append(city(inp,dist,lat,lng))
sortbydist = sorted(cities, key=lambda city: city.dist)
sortbybldist = sorted(cities, key=lambda city: city.bldist)
print 'Cities in order of distance by driving:'
for c in sortbydist:
    print '\t'+c.name+'\t'+str(c.dist)+ ' m'
print '\n'
print 'Cities in order of bird line distance:'
for c in sortbybldist:
    print '\t'+c.name+'\t'+str(c.bldist)+ ' m'


