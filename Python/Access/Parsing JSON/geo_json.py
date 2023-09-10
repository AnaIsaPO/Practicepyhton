import urllib.parse, urllib.request, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    #Ask for location
    address = input('Enter location: ') # Ann Arbor, MI
    if len(address) < 1:
        break
    #Make a URL
    url = serviceurl +  urllib.parse.urlencode({'address' : address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    #We call the data with .read()
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    print('lat', lat)