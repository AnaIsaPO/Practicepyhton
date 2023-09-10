#Open files
handle = open('d:\Ana Isabel\Documents\Python\Data Structures\Files\words.txt')
print(handle)

#Newline Character
stuff = 'Hello \n World'

#File Handle as a Sequence
for cheese in handle:
    print(cheese)

#Counting Lines in a File
count = 0
for line in handle:
    count = count + 1
print('Line count: ', count)

#Read the whole file
inp = handle.read()
print(len(inp))
print(inp[:20])

#Searching Through a File
for line in handle:
    if line.startswith('and'):
        print(line)

#We can strip the whitespace using rstrip()
for line in handle:
    line = line.rstrip()
    if line.startswith('to'):
        print(line)

#Skipping with continue
for line in handle:
    line = line.rstrip()
    if not line.startswith('are'):
        continue
    print(line)

#Using in to Select lines
for line in handle:
    line = line.rstrip()
    if not 'the' in line:
        continue
    print(line)

#Prompt for File Name
fname = input('Enter the file name: ')
fhand = open(fname)
counta = 0
for line in fhand:
    if line.startswith('do'):
        counta = counta + 1
print('There were', counta, 'do lines in', fname)

#Bad File Names
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be oppened:', fname)
    quit()  #Exit the program
counti = 0
for line in fhand:
    if line.startswith('someone'):
        counti = counti + 1
print('There were', counti, 'someone lines in', fname)