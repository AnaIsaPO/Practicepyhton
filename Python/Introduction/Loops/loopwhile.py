#Loops (repeated steps) have iteration 
#variables that change each time through a loop

n = 5
while n > 0 :
    print(n)
    n = n-1
print("Blastoff!")
print(n)

#Breaking out of a loop
while True:
    line = input("> ")
    if line == "done" :
        break
    print(line)
print("Done")

#Finishing an iteration with continue
while True:
    line = input("> ")
    if line[0] == "#" :
        continue
    if line == "done" :
        break
    print(line)
print("Done")