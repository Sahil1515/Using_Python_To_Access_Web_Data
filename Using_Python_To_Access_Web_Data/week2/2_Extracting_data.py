import re as re

x='My 2 favourite numbers are 19 and 42'
y=re.findall('[0-9]+',x)
print(y)

y=re.findall('[AEIOU]+',x)
print(y)

# Greedy Matching
x='From: Using the : character'
y=re.findall('^F.+:',x)
print(y)

#Non-Greedy Matching
x='From: Using the : character'
y=re.findall('^F.+?:',x)
print(y)

x='From sahilsainisalaria@gmail.com sat Jan 5 09:14:16 2008'
y=re.findall('\\S+@\\S+',x)# we need to use only \S but single \ gives warning so i used \\
print(y)

y=re.findall('\\S+(\\S@\\S+?)',x)# Applying the non-greedy method of extracting 
print('\n Me trying')
# y=re.findall('\\S+?@\\S+',x)
print(y)

# Using parenthesis
print('\n# Using parenthesis')
y=re.findall('^From (\\S+@\\S+)',x)
print(y)

# Finding after the @: gmail.com
y=re.findall('@(\\S+)',x)
print(y)
#or
y=re.findall('@([^ ]*)',x)# [^ ] means some non-blank character
print(y)

# Floating point number
x='3.443 2.5656 0.323 $100'
y=re.findall('[0-9.]+',x)
print(y)

# Searching some predefined character like $
x='3.443 2.5656 0.323 $100'
y=re.findall('\\$[0-9.]+',x)# using \$ or \\$: which means really a dollar sign
print(y)