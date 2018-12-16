import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors',context=ssl_context)
bs = BeautifulSoup(html,'html.parser')
table = bs.findAll('table',{'class':'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('editors.csv','wt+')

writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)

finally:
    csvFile.close()