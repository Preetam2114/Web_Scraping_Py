from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random 
import pymysql
import re
import ssl

conn = pymysql.connect('localhost','root','PVR@ne2114','scraping')
cur = conn.cursor()
cur.execute('USE scraping')

random.seed(datetime.datetime.now())
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
def store(title,content):
    cur.execute('INSERT INTO pages (title,content) VALUES ("%s","%s")',(title,content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org'+articleUrl,context=ssl_context)
    bs = BeautifulSoup(html,'html.parser')
    title = bs.find('h1').get_text()
    content = bs.find('div',{'id':'mw-content-text'}).find('p').get_text()
    store(title,content)
    return bs.find('div',{'id':'mw-content-text'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/kevin_Bacon')

try:
    while len(links)>0:
        newArticle = links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)

finally:
    cur.close()
    conn.close()

