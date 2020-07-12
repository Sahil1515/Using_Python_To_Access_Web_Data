import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

data=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_200412.html')

soup=BeautifulSoup(data,'html.parser')
print("\n\nPrinting the HTML Parser:\n\n")
print(soup)

print("\n\nPrinting the tr parser:\n\n")
all_data_tr=soup.find_all('tr')[1:] #Not required actually
print(all_data_tr)

print("\n\nPrinting the td parser:\n\n")
all_data_td=soup.find_all('td')[1:]
print(all_data_td)

print("\n\n\n\n")

list1=[]
for i in range(2,len(all_data_td),2):
    list1.append(all_data_td[i].get_text())
print(list1)

sum=0
for i in list1:
    sum=sum+int(i)
print(sum)