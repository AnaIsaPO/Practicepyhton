#Pull the hour out 
name = input("Enter file:") #d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith('From '):
        sline = line.split()
        hline = sline[5]
        hour = hline.split(':')
        shour = hour[0]
        print('Hour: ',shour)
        counts[shour] = counts.get(shour, 0) + 1
print(counts)

lst = list()
for k, v in counts.items():
    newtup = (k,v)
    lst.append(newtup)

newhour = sorted(lst)
print(newhour)

for date in newhour:
    print(date)

for key, val in newhour:
    print('Min hour to max hour',key, val)

#Inverse the value
rlist = list()
for rkey, rval in newhour:
    rtup = (rval, rkey)
    rlist.append(rtup)
    #print(rval, rkey)
rev = sorted(rlist, reverse=True)
#print(rev)

for num,charac in rev:
    print('Max times of hour to min',charac, num)