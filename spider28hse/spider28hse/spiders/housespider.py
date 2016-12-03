# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

from spider28hse.items import Spider28HseItem

class housespider(CrawlSpider):
	name = "housespider"
	allowed_domains = ["28hse.com"]
	start_urls = ['http://www.28hse.com/en']
	
	rules = (
		Rule(LinkExtractor(allow=['en/buy-property']),callback='parse_item',follow=True),
	)
	
	def parse_item(self, response):
		item = Spider28HseItem()
		
		table = response.xpath("//*[@id='bA']/div[2]/div[2]/ul/li[1]/div/div[2]/table")
		
		web_names=['Property ID','Status','Price','Floor','Gross area(sq feet)','Net floor area(sq feet)','Property age(year)','Address','Expire date','Room']
		item_keys=['propertyid', 'Status','Price', 'Floor' ,'GrossArea', 'NetArea', 'Age', 'Address', 'Date', 'Room']
		for name,key in zip(web_names, item_keys):
			if table.xpath(".//tr[th/text()='%s']/td" % name):
				item[key]=table.xpath(".//tr[th/text()='%s']/td" % name).extract()
		
		return item
