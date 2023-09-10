#Counting
cc = dict()
cc['csev'] = 1
cc['cwen'] = 1
print(cc)

cc['cwen'] = cc['cwen'] + 1
print(cc)

#Count name in dictionary
counts = dict()
names = ['Pedro', 'Juan', 'Rebeca', 'Ben', 'Annie', 'Rebeca']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#The 'GET' method for Dictionaries -> checking to see if a key is alredy in a dictionary
if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name, 0) #get(key, default)
print(x)

#Count name in dictionary with GET
counts = dict()
names = ['Pedro', 'Juan', 'Rebeca', 'Ben', 'Annie', 'Rebeca']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)