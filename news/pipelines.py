# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class NewsPipeline(object):
#     def process_item(self, item, spider):
#         return item

import csv
import settings
import time
import os.path


class WriteToCsv(object):

    def __init__(self):
    	csvname = 'pipe_out_'+time.strftime("%Y+%m+%d")+'.csv'
    	self.csvname = csvname
    	if os.path.isfile(csvname) == True:
        	self.csvwriter = csv.writer(open(csvname, 'a'))
        	self.file_existed = True
        else:
        	self.csvwriter = csv.writer(open(csvname,'w'))
        	self.file_existed = False
        
    def process_item(self, item, newsgen):
    	if self.file_existed==True:
	        self.csvwriter.writerow([item['title'][0],item['url'][0],item['desc'][0],item['author'][0],item['source'][0],item['datetime'][0],item['arttype'][0],item['site'][0],item['text']])
        else:
        	self.csvwriter.writerow(['TITLE','URL','DESCRIPTION','AUTHOR','SOURCE','DATETIME','ARTICLE TYPE','SITE','TEXT RE: NOTRE DAME'])
        	self.csvwriter.writerow([item['title'][0],item['url'][0],item['desc'][0],item['author'][0],item['source'][0],item['datetime'][0],item['arttype'][0],item['site'][0],item['text']])
        return item

### THIS CRAWLER PIPELINE FROM
### http://stackoverflow.com/questions/20753358/how-can-i-use-the-fields-to-export-attribute-in-baseitemexporter-to-order-my-scr/20758558#20758558

# from scrapy import signals
# from scrapy.contrib.exporter import CsvItemExporter

# class CSVPipeline(object):

#   def __init__(self):
#     self.files = {}

#   @classmethod
#   def from_crawler(cls, crawler):
#     pipeline = cls()
#     crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
#     crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
#     return pipeline

#   def spider_opened(self, spider):
#     file = open('%s_items.csv' % spider.name, 'w+b')
#     self.files[spider] = file
#     self.exporter = CsvItemExporter(file)
#     self.exporter.fields_to_export = [list with Names of fields to export - order is important]
#     self.exporter.start_exporting()

#   def spider_closed(self, spider):
#     self.exporter.finish_exporting()
#     file = self.files.pop(spider)
#     file.close()

#   def process_item(self, item, spider):
#     self.exporter.export_item(item)
#     return item