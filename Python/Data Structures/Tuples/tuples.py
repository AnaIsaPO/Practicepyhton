#Tuples are another kind of sequence
#Tuples are no 'immutable' -> you can't change the content
(x,y) = (4, 'fred')
print(x,y)

#Tuples and comparable
(0, 1, 2) < (4, 5, 6)

#Sorting list of tuples
d = {'a':10, 'b':1, 'c':22}
d.items()
s = sorted(d.items())
print(s)
for k,v in s:
    print(k,v)

tmp = list()
for k,v in d.items():
    tmp.append((v,k))
print(tmp)

rev = sorted(tmp, reverse=True)
print(rev)

#The top 10 most common words
name = input("Enter file:") #d:\Ana Isabel\Documents\Python\Data Structures\Files\romeo.txt
handle = open(name)

counts = dict()

#Get an histogram
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1   

#List of tuples
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

#High value to the soft value
lst = sorted(lst, reverse=True)
#print(lst)

#Select the first 10 higher values
for val, key in lst[:10]:
    print(key, val)

#Shorter version
print(sorted([(v,k) for k,v in counts.items()]))