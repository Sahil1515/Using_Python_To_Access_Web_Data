import re as re
import wikipedia as wikipedia

# msg=wikipedia.search('Sahil')[0]
# data=wikipedia.page(msg)
# print(data.content)

data=open('f.txt')
# print(data.read())
for line in data:
    line=line.rstrip()
    if re.search('^What',line):
    # if re.search('^X-\S+:',line):
        print(line)

