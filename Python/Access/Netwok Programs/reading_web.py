import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

counts = dict()
for line in fhand:
    print(line.decode().strip())