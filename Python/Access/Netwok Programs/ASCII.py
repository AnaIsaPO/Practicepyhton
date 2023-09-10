#Each character is represented by a number between 0 and 256
#stored in 8 bits of memory (my disk drive contains 3 Terabytes of memory)

#The ord function tells us the numeric value of a simple ASCCI character
print(ord('l'))
print(ord('G'))
print(ord('\n'))
print(ord('*'))
print(chr(105))

#Multi-Byte characters
#The byte string and the regular string are different
#The regular string and the Unicode string are the same

#When we read data we must decode it

#Ans HTTP Request in Python



#FROM ASCII TO STRING 

# Input list
lst = [80, 121, 116, 104, 111, 110,
        80, 111, 111, 108]
 
# Printing initial list
print ("Input list", lst)
 
# Using chr() Method
res = ""
for i in lst:
    res = res + chr(i)
 
print ("String : ", str(res))