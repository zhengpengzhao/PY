import requests
r = requests.get('https://music.163.com/')
demo=r.text
#print(demo)
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
print(r.content)
print(r.headers)

from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,'html.parser')
print(soup.a)
print(soup.title)


