# -*- coding: utf-8 -*-
# -----import-----
import scrapy
from scrapy.spider import CrawlSpider, Rule  
from scrapy.selector import Selector  
from scrapy.linkextractors import LinkExtractor

from spider28hse.items import Spider28HseItem
# -----import-----

class houseSpider(CrawlSpider):
    # spider starts from homepage
	name = "housespider"
    allowed_domains = ["28hse.com"]
    start_urls = ['http://www.28hse.com/']
	# get url with rules below, and parse it using parse_item
	rules=(LinkExtractor(allow=('buy-property-', )),callback='parse_item')
	
    def parse_item(self, response):
        item=Spider28HseItem()
		item['']=response.xpath #extract items from responses
		
		
		pass
