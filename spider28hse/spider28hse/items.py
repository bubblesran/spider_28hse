# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider28HseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	ID=scrapy.Field()
	Status=scrapy.Field()
	Price=scrapy.Field()
	Floor=scrapy.Field()
	Area=scrapy.Field()
	Age=scrapy.Field()
	Address=scrapy.Field()
	Date=scrapy.Field()
	Rooms=scrapy.Field()
	Describe=scrapy.Field()
    pass
