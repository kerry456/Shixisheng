#!/usr/bin/env python
#coding:utf-8
from shixisehng.spiders.redis_shixi import RedisShixiSpider

from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings

# 获取settings.py模块的设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)


# 可以添加多个spider0ehp
process.crawl(RedisShixiSpider)


# 启动爬虫，会阻塞，直到爬取完成
process.start()

