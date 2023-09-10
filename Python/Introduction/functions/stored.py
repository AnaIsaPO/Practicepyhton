#Function to print
def thing():
    print("Hello")
    print("Fun")

thing()
print("ZIP")
thing()

#Print the max character in the argument 
big = max("hello world")
print(big)

tiny = min("hello world")
print(tiny)

#Function sum
def sum():
    x = input('Enter a number: ')
    x = int(x)*5
    print(x)

sum()

def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")

greet("fr")

#Function with return 
def again():
    return "Hello"

print(again(), "Annie")

#Multiple parameters 
def addtwo(a, b):
    added = a + b
    return added
y = addtwo(3, 5)
print(y)

def stuff():
    print("Hello")
    return
    print("World")

stuff()

