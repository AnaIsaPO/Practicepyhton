import xml.etree.ElementTree as ET
#Tree ''' indicates that we'll write a multiple lines 
data = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
    </users>
</stuff>'''

#To take a string data we use .fromstring to convert data to tree information
stuff = ET.fromstring(data)
#Search for users/user text --> Tag are a list 
lst = stuff.findall('users/user')
#We print how many there are
print('User count:', len(lst))
#We call that TAG and print info
for item in lst:
    print('Name:', item.find('name').text)
    print('Id', item.find('id').text)
    print('Atribute:', item.get("x"))