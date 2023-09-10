astr = "hi"
try :
    istr = int(astr)
except :
    istr = -1

print("Second", istr)

#Anothe sample try

num = input("Enter a number: ")
try:
    new = int(num)
except:
    new = -1

if new > 0 :
    print("Nice work!")
    print("Still work")
    print("It's a number")
else: 
    print("Not a number")