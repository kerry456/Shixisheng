# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
import re
from shixisheng.shixisehng.items import ShixisehngItem
from urllib import parse
from scrapy_redis.spiders import RedisSpider
from redis import Redis
identified = 'master'
from scrapy.selector import Selector

from shixisehng.respone_replace import *

from lxml import etree


class RedisShixiSpider(RedisSpider):
    name='master'
    allowed_domains=['shixiseng.com']
    r = Redis(host='',port=6379,password='123456')
    # r =  Redis()
    def start_requests(self):
        base_url = 'https://www.shixiseng.com/interns?k={}&p={}'
        key_words = parse.quote(self.settings['LOCATION'])
        if identified == 'master':
            for i in range(1,10):
                url = base_url.format(key_words,str(i))
                # self.r.lpush(self.redis_key,url)
                # urls = self.r.lrange('shixisheng:start_urls',0,-1)
                # for Url in urls:
                # Urls = self.r.brpoplpush(self.redis_key,'shixisheng:master',3)
            # for us in Urls[::-1]:
                yield scrapy.Request(url=url,callback=self.parse)
        exit(0)
        # self.redis_key = 'shixisheng:start_urls'

    #//div[@class ="position"]//a[@ class ="name"]/@href

    def parse(self, response):

        res = Selector(response)
        url_list = response.xpath('//div[@class="position"]//a[@class="name"]/@href').extract()
        for x in url_list:
            url = 'https://www.shixiseng.com' + x
            self.r.lpush(self.redis_key,url)
            yield scrapy.Request(url=url,callback=self.parse_item)



    def parse_item(self,response):

        item = ShixisehngItem()

        response = response.text.replace('&#xf66a', '1').replace('&#xed6a', '0') \
            .replace('&#xe8e6', '7').replace('&#xeb83', '3') \
            .replace('&#xe5d0', '4').replace('&#xed6a', '6') \
            .replace('&#xe87f', '0').replace('&#xe363', '1')\
            .replace('&#xf77c', '2').replace('&#xeb83', '3')\
            .replace('&#xf3a5', '4').replace('&#xeb07', '5')\
            .replace('&#xe2e2', '6').replace('&#xe71e', '7')\
            .replace('&#xe84e', '8').replace('&#xf18c', '9').replace('僧','生')




        # respon = decyrpt_text(response)

        select = etree.HTML(response,parser=etree.HTMLParser(encoding='utf-8'))

        item['name'] = select.xpath('//div[@class="new_job_name"]/text()')[0].strip() \
            if select.xpath('//div[@class="new_job_name"]/text()') else  ''
        try:
            item['salary'] = select.xpath('//div[@class="job_msg"]/span[1]/text()')[0].strip()
        except:
            item['salary'] = ''
        try:
            item['location'] = select.xpath('//div[@class="job_msg"]/span[2]/text()')[0].strip()
        except:
            item['location'] = ''
        try:
            item['xueli'] = select.xpath('//div[@class="job_msg"]/span[3]/text()')[0].strip()
        except:
            item['xueli'] = ''
        try:
            item['worktime'] = select.xpath('//div[@class="job_msg"]/span[4]/text()')[0].strip()
        except:
            item['worktime'] = ''
        try:
            item['time'] = select.xpath('//div[@class="job_msg"]/span[5]/text()')[0].strip()
        except:
            item['time'] = ''
        try:
            item['category'] = select.xpath('//div[@class="job_detail job_detail_msg"]/span[3]/text()')[0].strip()
        except:
            item['category'] = ''
        try:
            item['required'] = select.xpath('string(//div[@class="job_detail"]//div)')[0].strip()
        except:
            item['required'] = ''
        yield item
