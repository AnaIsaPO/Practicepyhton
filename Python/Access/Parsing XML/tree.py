import xml.etree.ElementTree as ET
#Tree ''' indicates that we'll write a multiple lines 
data = '''<person>
    <name>Chuck</name>
    <phone type ="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
    </person>'''

#To take a string data we use .fromstring to convert data to tree information
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))