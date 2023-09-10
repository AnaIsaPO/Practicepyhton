import json
#We have 2 dictionaries
input = '''[
    {"id" : "001",
     "x" : "2",
     "name" : "Chuck"
    },
    {"id" : "009",
     "x" : "7",
     "name" : "Chuck"
    }
]'''
#Info is a list with 2 dictionaries
info = json.loads(input)
print('User count:', len(info))
for item in info:
    #Every dictionary have 2 tuples
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])