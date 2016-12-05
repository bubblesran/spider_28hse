# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item


class Spider28HseItem(Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	propertyid=scrapy.Field()
	Status=scrapy.Field()
	Price=scrapy.Field()
	Block=scrapy.Field()
	Floor=scrapy.Field()
	GrossArea=scrapy.Field()
	NetArea=scrapy.Field()
	Age=scrapy.Field()
	Address=scrapy.Field()
	Date=scrapy.Field()
	Room=scrapy.Field()