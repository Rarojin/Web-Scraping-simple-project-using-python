import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.webfx.com/blog/web-design/30-beautiful-clean-and-simple-web-designs-for-inspiration/')
soup= BeautifulSoup(r.content, features='html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))