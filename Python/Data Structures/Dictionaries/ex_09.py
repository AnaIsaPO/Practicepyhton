name = input("Enter file:") #d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt
handle = open(name)

di = dict()
for lin in handle:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        #print(w)
        if w in di:
            di[w] = di[w] + 1
            #print('**Existing**')
        else:
            di[w] = 1
            #print('**New**')
        #print(di[w])
print(di)