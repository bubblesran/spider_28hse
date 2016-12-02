# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector

from scrapy.linkextractors import LinkExtractor
from spider28hse.items import Spider28HseItem

class houseSpider(CrawlSpider):
	name = "housespider"
	allowed_domains = ["www.28hse.com"]
	start_urls = ['http://www.28hse.com']
	rules = (
		Rule(LinkExtractor(allow=('buy-property-'))),
		Rule(LinkExtractor(allow=('buy-property-')),callback='parse_item')
	)
	def parse_item(self, response):
		item = Spider28HseItem()
		item['id'] = response.xpath("//*[@id='bA']/div[2]/div[2]/ul/li[1]/div/div[2]/table/tr[1]/td/text()").extract()
		item['Status']=response.xpath("//*[@id='bA']/div[2]/div[2]/ul/li[1]/div/div[2]/table/tr[2]/td/font/text()").extract()
		return item