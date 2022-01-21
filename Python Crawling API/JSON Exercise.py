import urllib.request, urllib.parse, urllib.error
import json

### First Assignment

url = input('Enter location: ') # http://py4e-data.dr-chuck.net/comments_1466785.json
    
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
    
info = json.loads(data)
print('Count:', len(info["comments"]))
    
numbers = [item['count'] for item in info["comments"]]
    
print('Sum: ', sum(numbers))


### Second Assignment

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')
    
parms = dict()
parms['address'] = address
parms['key'] = 42
url = serviceurl + urllib.parse.urlencode(parms)
    
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
   
print('Place id', js["results"][0]["place_id"])