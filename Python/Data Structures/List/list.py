#Using the Range Function | Returns a list of numbers
print(range(4))

#Concatenating Lists Using "+"
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

#List can be sliced using ":"
t = [9, 8, 7, 15, 48, 65, 21] 
print(t[1:3]) #up to but not including 

#Building an empty list and then add elements using the "append" method
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

#List can be sorted (change its order)
friends = ['Juan', 'Maria', 'Pedro', 'Pablo', 'Annie', 'Luis', 'Alejandra', 'Ruben']
print(friends)
friends.sort()
print(friends)

#Built-in Functions and Lists
nums = [3, 41, 89, 2, 35, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))

#Obtain average with count
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average', average)

#Obtain average with append <- require memory
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print(numlist)
print('Average', average)