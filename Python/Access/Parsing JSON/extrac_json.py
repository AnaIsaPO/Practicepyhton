import urllib.parse, urllib.request, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

numlist = list()

while True:
    url = input('Enter data: ') #http://py4e-data.dr-chuck.net/comments_42.json
    #data:  http://py4e-data.dr-chuck.net/comments_1615036.json
    if len(url) < 1: 
        break

    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None

    #print(js)
    for item in js['comments']:
        #print(item)
        count = item['count']
        #lng = js['comments'][0]['count']
        #print('count', count)
        num = int(count)
        numlist.append(num)  
        add = sum(numlist)
    print(add)


