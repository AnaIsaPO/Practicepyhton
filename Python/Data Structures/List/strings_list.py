#Split breaks a string into parts
abc = 'With three words'
stuff = abc.split()
print(stuff)

for w in stuff:
    print(w)

print(stuff[1])

#Delimiter
line = 'first;second;third'
thing = line.split(';')
print(thing)

#Find 
fname = input("Enter file name: ") # d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    print(words[2])

#The double split pattern 
email = words[1]
pieces = email.split('@')
print(pieces[1])