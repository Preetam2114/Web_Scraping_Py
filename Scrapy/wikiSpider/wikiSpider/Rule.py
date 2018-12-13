from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule

class ArticleSpyder(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'.*'),callback='parse_item',follow=True)]

    def parse_items(self,response):
    	url = response.url
    	title = response.css('h1::text').extract_first()
    	text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
    	lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
    	lastUpdated = lastUpdated.replace('this page was last editted on','')
    	print('url is :'.format(url))
    	print('title is :'.format(title))
    	print('text is :'.format(text))
    	print('last updated:'.format(lastUpdated))
