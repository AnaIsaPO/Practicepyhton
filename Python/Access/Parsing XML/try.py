import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#http://py4e-data.dr-chuck.net/comments_42.xml
data = urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_1615035.xml ') # http://py4e-data.dr-chuck.net/comments_1615035.xml
rdata = data.read()

print('Retrieved', len(rdata), 'characters')
print(rdata.decode())

tree = ET.fromstring(rdata)
lst = tree.findall('comments/comment')
numlist = list()

for item in lst:
    numbers = item.find('count').text
    #print(numbers)
    num = int(numbers)
    numlist.append(num)  
    add = sum(numlist)
print(add)


