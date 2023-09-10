#Retrieving web pages with urllib
#The equivalent code to read the romeo.txt file from the web using urllib is as
#follows:

import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#the urllib code consumes the headers and only returns the data to us

##compute the frequency of each word in the file
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)