namehrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
if h > 40 :
    hn = h - 40
    pay = (hn*(r*1.5))+(40*r)
    print("Must pay: ", pay)
else:
    pay = h * r
    print("Must pay: ", pay)