# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys

from scrapy.exporters import CsvItemExporter
from scrapy.exceptions import DropItem
from scrapy import signals


class DuplicatesPipeline(object):

	def __init__(self):
		self.ids_seen = set()

	def process_item(self, item, spider):
		if item['propertyid'] in self.ids_seen:
			raise DropItem("Duplicate item found: %s" % item)
		else:
			self.ids_seen.add(item['propertyid'])
			return item

class ExportcsvPipline(object):
	@classmethod
	def from_crawler(cls, crawler):
		pipeline = cls()
		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
		crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
		return pipeline

	def spider_opened(self, spider):
		self.file=open('items.csv','wb')
		self.exporter = CsvItemExporter(self.file)
		self.exporter.start_exporting()
	
	def spider_closed(self, spider):
		self.exporter.finish_exporting()
		self.file.close()
		
	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item