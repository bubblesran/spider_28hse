# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
from scrapy.exporters import CsvItemExporter

class DuplicatesPipeline(object):

	def __init__(self):
		self.ids_seen = set()

	def process_item(self, item, housespider):
		if item['id'] in self.ids_seen:
			raise DropItem("Duplicate item found: %s" % item)
		else:
			self.ids_seen.add(item['id'])
			return item

class ExportcsvPipline(object):
	def spider_opened(self, housespider):
		self.file=open('items.csv','w')
		self.exporter = CsvItemExporter(self.file)
		self.exporter.start_exporting()
	
	def spider_closed(self, housespider):
		self.exporter.finish_exporting()
		self.file.close()
		
	def process_item(self, item, housespider):
		self.exporter.export_item(item)
		return item