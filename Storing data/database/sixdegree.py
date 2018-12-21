import re
import pymysql
from random import shuffle

conn = pymysql.connect('localhost','root','PVR@ne2114','wikipedia','utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')

def insertPageIfNotExists(url):
    cur.execute('SELECT * FROM pages WHERE url = %s',(url))
    if cur.rowcount == 0:
            cur.execute('INSERT INTO pages (url) VALUES (%s)',(url))
            conn.commit()
            return cur.lastrowid
    else:
            return cur.fetchone()[0]

def loadPages():
        cur.execute('SELECT * FROM pages')
        pages = [row[1] for row in cur.fetchall()]
        return pages

def insertLink(fromPageId,toPageId):
        cur.execute('SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s',(int(fromPageId),int(toPageId)))
        if cur.rowcount == 0 :
                cur.execute('INSERT INTO links (fromPageId,toPageId) VALUES (%s,%s)',(int(fromPageId),int(toPageId)))
                conn.commit()

def getLinks(pageUrl,recursionlevel,pages):
        cur.execute('')
