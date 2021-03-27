import requests
from bs4 import BeautifulSoup

def get_url(company):
    template='https://www.geeksforgeeks.org/{}-topics-interview-preparation/'
    url=template.format(company)
    return url

comapny=input()
url=get_url(company)
response=requests.get(url)
print(url)
soup=BeautifulSoup(response.text,'html.parser')
divi=soup.find('div',{'class':'entry-content'})
questions=[]
for tag in divi.find_all('a'):
    link=tag['href']
    text=link.replace('http://www.geeksforgeeks.org/','').replace('/','')
    question=(company,text,link)
    questions.append(question)
    
for i in range(3):
    questions.pop(0)
print(questions)