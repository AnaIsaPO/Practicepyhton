#Looking inside strings
fruit = 'banana'
#Banana
#012345
leter = fruit[0]
print(leter)
x=3
second = fruit[x-1]
print(second)

#Strings have length
print(len(fruit))

#Looping through strings
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

for leter in fruit:
    print(leter)

#Looping and counting
word = 'banana'
count = 0
for let in word:
    if let == 'a':
        count = count + 1
print(count)

#Looking deeper into in 
for letter in 'banana':
    print(letter)

#Slicing strings
h = 'Hello World'
print(h[:4])
print(h[5:])

