import pymysql
conn = pymysql.connect('localhost','root','PVR@ne2114','mysql')
cur = conn.cursor()
cur.execute('USE scraping')
cur.execute('SELECT id, title FROM pages WHERE content LIKE "%page content%"')
print(cur.fetchone())
cur.close()
conn.close()