#Counting in a loop
zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print("After", zork)

#Summing in a loop
zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print("After", zork)

#Finding the average in a loop
count = 0
sum = 0
print("Before", count, sum)
for thing in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + thing
    print(count, sum, thing)
print("After", count, sum, sum/count)