import json
import urllib2
import math
f = math.pi/180
Rearth=6371000
page = urllib2.urlopen('https://maps.googleapis.com/maps/api/directions/json?origin=IIT+Bombay&destination=IIT+Bombay')
resp = page.read()
data = json.loads(resp)
itheta = (90 - data['routes'][0]['legs'][0]['start_location']['lat'])*f
iphi = (data['routes'][0]['legs'][0]['start_location']['lng'] +180)*f
class city:
    def __init__(self, s, d, lt, lg):
        self.name = s
        self.dist = d
        if lt == 100 or lg == 100:
            self.bldist = 100000000
        else:
            theta = (90 - lt)*f
            phi = (lg + 180)*f
            dot = math.cos(theta)*math.cos(itheta)+math.sin(theta)*math.sin(itheta)*math.cos(iphi-phi)
            self.bldist = Rearth*math.acos(dot)
    def __repr__(self):
        return repr((self.name,self.dist))
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
            dist = 100000000
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
    print '\t'+c.name
print '\n'
print 'Cities in order of bird line distance:'
for c in sortbybldist:
    print '\t'+c.name


