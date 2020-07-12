from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
import pandas as pd 

# import requests 
# page.content

url=input("Enter the url: ")

pages=urllib.request.urlopen(url)
# for page in pages:
#     print(page.decode().rstrip())
soup=BeautifulSoup(pages,'html.parser')
data = soup.find_all('div')
all_data = soup.find_all('tr')[1:]
all_data_td = soup.find_all('td')[1:]
# print(all_data_td)

all_data_list=[]
for i in range(0,len(all_data_td)): 
    all_data_list.append(all_data_td[i].get_text())
# print(all_data_list)

states=[]
for i in range(0,len(all_data_list),5):
    states.append(all_data_td[i].get_text())
states=states[:-3]
# print(states,len(states))

confirmed=[]
for i in range(1,len(all_data_list),5):
    confirmed.append(all_data_td[i].get_text())
confirmed=confirmed[:-3]
# print(confirmed,len(confirmed))

cured=[]
for i in range(2,len(all_data_list),5):
    cured.append(all_data_td[i].get_text())
cured=cured[:-3]
# print(cured,len(cured))

deaths=[]
for i in range(3,len(all_data_list),5):
    deaths.append(all_data_td[i].get_text())
deaths=deaths[:-2]
# print(deaths,len(deaths))

df=pd.DataFrame()
df['States']=states
df['Confirmed']=confirmed
df['Cured']=cured
df['Deaths']=deaths

print(df)
df.set_index('States',inplace=True)
df=df.reset_index()
print(df)
df.sort_values('Confirmed',inplace=True)
print(df)
#   https://www.mohfw.gov.in/#