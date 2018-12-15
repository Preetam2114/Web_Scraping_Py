# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
from wikiSpider.items import Article
from string import whitespace

class WikispiderPipeline(object):
    def process_items(self,article,spider):
        #dateStr = article['lastUpdated']
        article['lastUpdated'] = article['lastUpdated'].replace('this page was last edited on ','')
        article['lastUpdated'] = article['lastUpdated'].strip()
        article['lastUpdated'] = datetime.strptime(article['lastUpdated'],'%d %B %Y, at %H:%M.')
        article['text'] = [line for line in article['text'] if line not in whitespace]
        article['text'] = ''.join(article['text'])
        return article
