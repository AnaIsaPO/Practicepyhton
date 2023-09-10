tot = 0
for i in [5, 4, 3, 2, 1]:
    tot = tot + 1
print(tot)

#Exercise 5.1

num = 0
tot = 0.0
while True:
    sval = input('Enter number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval 

print('All done')
print(tot, num, tot/num)