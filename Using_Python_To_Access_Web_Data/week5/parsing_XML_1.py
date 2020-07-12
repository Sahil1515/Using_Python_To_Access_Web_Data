import xml.etree.ElementTree as ET

data='''<person>
    <name>Sahil</name>
    <phone type="intl">
        +383278732938
    </phone>
    <email hide="yes"/>
    </person>'''

tree=ET.fromstring(data)
print('Name: '+tree.find('name').text)
print('Attribute: '+tree.find('email').get('hide'))