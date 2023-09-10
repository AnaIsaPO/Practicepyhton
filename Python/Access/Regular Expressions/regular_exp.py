#Using re.search Like find()
#re.search() returns a True/False depending on whether the string matches the regular expression
#If we actually want to matching strings to be extracted, we use re.findall()
hand = open('d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt')#d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt
for line in hand:
    line = line.rstrip()
    if line.find('From: ') >= 0:
        print('find',line)

import re
handle = open('d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt')
for lines in handle:
    lines = lines.rstrip()
    if re.search('From:', lines):
        print('Search',lines)


#Using re.search() Like find()
hand = open('d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt')#d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt
for line in hand:
    line = line.rstrip()
    if line.startswith('From: '):
        print('Startswith',line)

#We use ^ to match the starting position within the string
import re
handle = open('d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt')
for lines in handle:
    lines = lines.rstrip()
    if re.search('^From:', lines):
        print('Search ^',lines)

#Dot character matches any character

#If you add * character, the character is any number of times
# + one or more times

#\S -> Match any non-whitespace character
import re
handle = open('d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt')
for lines in handle:
    lines = lines.rstrip()
    if re.search('^R\S+:', lines):
        print('Search \S',lines)
#[] <- Square bracket define the number of digits (one or more digits)
x = 'My 2 favorite numbers are 198 and 42'
y = re.findall('[0-9]+', x)
print(y)


#The repeat characters (* and +) push outward in both directions 
#Largest version add (.)
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

#Shortest version add (?)
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

#Fine-Tuning string extraction
import re
x = 'From: gopal.ramasammycook@gmail.com Sat Jan'
y = re.findall('\S+@\S+', x)
print(y)

#Parentheses are not part of the match but they tell where to start and stop
import re
x = 'From: gopal.ramasammycook@gmail.com Sat Jan'
y = re.findall('^From: (\S+@\S+)', x)
print(y)

#The regex version 
import re 
lin = 'From: gopal.ramasammycook@uct.za.hey.com Sat Jan'
#[^ ] <- Match non-blanck characters
y = re.findall('@([^ ]*)', lin)
print(y)

#re.findall give you a list of strings