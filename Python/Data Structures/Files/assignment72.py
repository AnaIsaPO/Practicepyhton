# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ") # d:\Ana Isabel\Documents\Python\Data Structures\Files\mbox-short.txt
fh = open(fname)
count = 0
add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    xtra = line.find(':')
    fxtra = float(line[xtra + 1:])
    add = add + fxtra
print("Average spam confidence:", add/count)