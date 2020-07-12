import urllib.request,urllib.parse,urllib.error
import re
# Python has produced urlib to make socket communications and http communications lot more better

# To get all the links out of a webpage using urllib and regular expressions
fhand=urllib.request.urlopen('https://www.wikipedia.org/')
for line in fhand:
   myline=line.decode().strip()
   link=re.findall('href="(.*)"',myline)
   if len(link)>0:
    print(link)

