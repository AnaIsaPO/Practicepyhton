#Dictionaries are like bags - no order
purse = dict()
purse['monkey'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

#List have positions and dictionaries have labels 
name = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(name)

#Empty dictionary
empty = { }
print(empty)

#Error typing
stuff = dict()
print(stuff['candy'])