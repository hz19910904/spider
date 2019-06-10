# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class DoubanspiderPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        # 链接数据库
        client = pymongo.MongoClient(host=host, port=port)

        # 指向指定的数据库
        mdb = client[dbname]
        # 获取数据库里存放数据的集合
        self.port = mdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        data = dict(item)
        self.port.insert(data)
        return item
