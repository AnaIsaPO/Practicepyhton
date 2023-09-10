#String concatenation 
a = 'Hello '
b = a + 'There'
print(b)

#Using in as a logical operator
fruit = 'banana'
if 'a' in fruit:
    print('Found it')

#String Library
greet = ' Hello Bob '
zap = greet.lower()
uap = greet.upper()
print(zap)
print(greet)
print(uap)
#'capitañize', 'casefold', 'center', 'count',
#'encode', 'endswith', 'expandtabs', 'find',
#'format', 'replace', 'split', 'upper', 'translate'

#searching a string
pos = fruit.find('na')
print(pos)

#Search and replace
repl = greet.replace('Bob', 'Jane')
print(repl)

#Stripping whitespace
left = greet.lstrip()
print(left)
right = greet.rstrip()
print(right)
both = greet.strip()
print(both)

#Prefixes
line = 'Please have a nice day'
correct = line.startswith('Please')
print(correct)

#Parsing and extracting
data = 'From anapadilla@hotmail.com '
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)
print(data[16:20])

x = '40'
y = int(x) +2
print(y)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])