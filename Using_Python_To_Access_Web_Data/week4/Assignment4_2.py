# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
#  scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of 
# times and report the last name you find.
# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual 
# data you need to process for the assignment
# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter - ')
list1=[]
def anchor_function(url):
    data=urllib.request.urlopen(url)
    soup=BeautifulSoup(data,'html.parser')
    anchor_tags=soup('a')
    list1.clear()
    for line in anchor_tags:
       list1.append(line.get('href',None))
    return list1


list2=[]

for i in range(7):
    list2=anchor_function(url)
    url=list2[17]
    
l=re.findall('http://py4e-data.dr-chuck.net/known_by_(.*).html',url)

for i in l:
    print(i)

# # Actual link:
# # http://py4e-data.dr-chuck.net/known_by_Adenn.html 

# # Sample link:
# # http://py4e-data.dr-chuck.net/known_by_Fikret.html




# Other temporary solution:

# import urllib.request,urllib.parse,urllib.error
# from bs4 import BeautifulSoup
# import re

# url = input('Enter - ')

# def anchor_function(url):
#     data=urllib.request.urlopen(url)
#     soup=BeautifulSoup(data,'html.parser')
#     anchor_tags=soup('a')
#     return anchor_tags

# list1=[]
# i=0
# me='http://py4e-data.dr-chuck.net/'
# # for tag in anchor_function(url):
# for i in range(7):
#     list1=anchor_function(url)
#     # print(list1)
#     you=me
#     you=you+'known_by_'+list1[17].get_text()+'.html'
#     url=you
#     # print(url)
#     # print('\n\n\n\n\n\n')
    

# l=re.findall('http://py4e-data.dr-chuck.net/known_by_(.*).html',url)

# for i in l:
#     print(i)

    



