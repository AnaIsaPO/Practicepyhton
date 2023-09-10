#Who has sent the greatest number of mail messages
name = input("Enter file:") #d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt
handle = open(name)

bigword = None
bignum = 0
senders = dict()
for line in handle:
    if line.startswith('From '):
        rline = line.rstrip()
        sline = rline.split()
        key = sline[1]
        #print(key)
        senders[key] = senders.get(key, 0) + 1

#print(senders)

for send,count in senders.items():
    if count > bignum:
        bignum = count
        bigword = send

print(bigword, bignum)