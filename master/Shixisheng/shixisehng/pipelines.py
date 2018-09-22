# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymongo
from pymongo import MongoClient

from shixisehng.spiders.redis_shixi import identified


class ShixisehngPipeline(object):
    def open_spider(self,spider):
        pass
    def process_item(self, item, spider):
        print({"name": item['name'], "salary": item['salary'], "location": item['location'], "xueli": item['xueli'],\
                                    "time": item['time'], "category": item['category'],"required": item['required']})
        return item



class MongoDBPipline(object):
    def open_spider(self,spider):
        try:
            if identified == 'master':
                self.client = MongoClient(host=self.settings['MONGO_HOST'],port=27017)
                self.shixisheng = self.client['test']['shixisheng']
                # print('ssssss')
            else:
                pass
            # self.collections = self.shixisheng
        except Exceptionas as e:
            print(e)

    def process_item(self,item,spider):
        self.insert_to_mongodb(item)
        print('数据插入成功....')
        return item


    def insert_to_mongodb(self, item):
        self.shixisheng.insert_one({"name": item['name'], "salary": item['salary'], "location": item['location'], "xueli": item['xueli'],\
                                    "time": item['time'], "category": item['category'],"required": item['required']})



# if __name__ == '__main__':
#     s = MongoDBPipline()
#     s.open_spider('ss')









