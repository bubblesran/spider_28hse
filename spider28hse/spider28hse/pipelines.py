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
		if item['ID'] in self.ids_seen:
			raise DropItem("Duplicate item found: %s" % item)
		else:
			self.ids_seen.add(item['ID'])
			return item

class ExportcsvPipline(object):
	def __init__(self):
		self.csvwriter = csv.writer(open('items.csv','w'))
		
	def process_item(self, item, housespider):
		row=item['ID']
		self.csvwriter.writerow(row)
		return item