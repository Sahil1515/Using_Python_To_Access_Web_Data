import xml.etree.ElementTree as ET 
import urllib.request,urllib.parse

data=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_200414.xml')

# Converting the HTTP object data to the string format
string=""
for line in data:
    string=string+line.decode().strip()+'\n'
# print(string)

# Making the tree from the XML string object
tree=ET.fromstring(string)

# Extracting the comments/comment section
lst=tree.findall('comments/comment')# This means comments->comment
# print(lst)

# Extracting the count text from the list containing all the comment sections
lst3=[]
for i in lst:
    lst3.append(i.find('count').text)

sum=0
for i in lst3:
    sum=sum+int(i)
print(sum)