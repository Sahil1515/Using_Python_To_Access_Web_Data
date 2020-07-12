# import requests
# page=requests.get('https://medium.com/better-humans/11-ninja-tips-on-how-to-wake-up-early-58d63d3972f3')
# print(page.content)

import urllib.request,urllib.parse,urllib.error
 
fhand=urllib.request.urlopen('http://data.pr4e.org/words.txt')

# Getting the data out of the fhand object
for line in fhand:
    print(line.decode().rstrip())

