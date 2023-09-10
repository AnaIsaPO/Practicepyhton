import re
handle = open('d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt')
numlist = list()
for line in handle:
    line = line.rstrip()
    #Search for lines that start whit X-DSPAM-Confidence: then follow by 0-9. 
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximun: ', max(numlist))

#When you add '\' after a sign this mean that you are looking for the sign 
#For example: \$ <- You are looking for the '$' character
