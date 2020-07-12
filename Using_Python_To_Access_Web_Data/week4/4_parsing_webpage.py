# What is web scrapping?

# when a program or script pretends to be a browser and retrieves web pages,
#looks at those web pages, extracts info, and then looks at more web pages 

# Search engines scrap web pages - we call this 'spidering the web' or 'web crawling'

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

# To get all the links out of a webpage using urllib and BeautifulSoup

url=input("Enter the url:")
fhand=urllib.request.urlopen(url).read() # .read() to get data as well
soup=BeautifulSoup(fhand,'html.parser')
# print(soup)
print("\n\n\n\n\n\n\n\n\n\n")
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))
    # print(tag)

print("\n\n\n\n\n\n\n\n\n\n")

table=soup('td')
for ele in table:
    print(ele.get('tr',None))
# https://www.wikipedia.org/
