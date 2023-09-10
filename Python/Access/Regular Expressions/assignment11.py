import re
#handle = open('D:\Ana Isabel\Documents\Python\Data\\regex_sum_42.txt')
handle = open('D:\Ana Isabel\Documents\Python\Data\\regex_sum_1615031.txt')
rhandle = handle.read()
numlist = list()

nstuff = re.findall('[0-9]+', rhandle)

for number in nstuff:
    num = int(number)
    numlist.append(num)  
    add = sum(numlist)
print(add)