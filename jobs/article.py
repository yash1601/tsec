import requests
from bs4 import BeautifulSoup

def get_url(company):
    template='https://www.geeksforgeeks.org/tag/{}/'
    url=template.format(company)
    return url

company=input()
url=get_url(company)
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
divi=soup.find_all('div',{'class':'content'})
articles=[]
for i in divi:
    try:
        content=i.text.split('Read More')[0]
        roundname=i.a.text
        links=i.a['href']
        text=content.replace(roundname,'')
        article=(company,text,roundname,links)
        articles.append(article)
    except:
        pass
print(articles)
