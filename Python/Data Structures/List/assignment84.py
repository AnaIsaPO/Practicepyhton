fname = input("Enter file name: ") #d:\Ana Isabel\Documents\Python\Data Structures\Files\romeo.txt
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    sline = line.split()
    for i in sline:
        if i in lst:
            continue
        else:
            lst.append(i)
    lst.sort()
    
print(lst)