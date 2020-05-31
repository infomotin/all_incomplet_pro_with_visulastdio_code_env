# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class DemoProjectPipeline:
#     def process_item(self, item, spider):
#         return item
from pymongo import MongoClient
class MongoDbPipline(object):
    collection = 'Quotes'
    #another Way to connet database and collections from setting 
    # def __init__(self,mongo_uri,mongo_db):
    #     self.mongo_uri = mongo_uri
    #     self.mongo_db = mongo_db
    # @classmethod
    # def from_crawler(cls,crawler):
    #     return cls(
    #         mongo_uri = crawler.setting.get('MONGO_URI'),
    #         mongo_db= crawler.setting.get('MONGO_DB')
    #         )




    def __init__(self):

        self.mongo_uri = 'mongodb://localhost:27017'
        self.mongo_db = 'goodreads'
    def open_spider(self,spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def close_spider(self,spider):
        self.client.close()
    def process_item(self, item, spider):
        self.db[self.collection].insert_one(dict(item))
        return item