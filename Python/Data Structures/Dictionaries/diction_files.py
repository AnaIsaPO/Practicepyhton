#Counting pattern
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

#Definite Loops and Dcitionaries
name = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in name:
    print(key, name[key])

#List of keys, values or items(both) from dictionaries
print(name)
print(name.keys())
print(name.values())
print(name.items())

#Two oiterations variables (keys, values)
for aa,bb in name.items():
    print(aa, bb)

#Example looking for the biggest word in the text
fname = input('Enter file:')
handle = open(fname)

count = dict()
for row in handle:
    characters = row.split()
    for charac in characters:
        count[charac] = count.get(charac, 0) + 1

bigcount = None
bigword = None
for first,second in count.items():
    if bigcount is None or second > bigcount:
        bigword = first
        bigcount = second
print(bigword, bigcount)