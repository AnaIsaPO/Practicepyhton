fname = input("Enter file name: ") #d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt
fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    sname = line.split()
    print(sname[1])
    count = count +1
    

print("There were", count, "lines in the file with From as the first word")


