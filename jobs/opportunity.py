import requests
from bs4 import BeautifulSoup

def get_url(position,location):
    template='https://in.indeed.com/jobs?q={}&l={}'
    url=template.format(position,location)
    return url

position=input()
location=input()
url=get_url((position).replace(' ','+'),location)
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
cards=soup.find_all('div','jobsearch-SerpJobCard')

def get_record(card):
     atag=card.h2.a
     jobtitle=atag.get('title').strip()
     joburl='http://www.indeed.com'+atag.get('href')
     company=card.find('span','company').text.strip()
     joblocation=card.find('div','recJobLoc').get('data-rc-loc')
     summary=card.find('div','summary').text.strip()
     if(card.find('span','salaryText') is not None):
         salary=card.find('span','salaryText').text.strip()
     else:
         salary=''
     post_date=card.find('span','date').text
     record=(jobtitle,joburl,company,joblocation,summary,salary,post_date)
     print(record)
     return record

records=[]
for card in cards:
     record=get_record(card)
     records.append(record)
print(records)
    