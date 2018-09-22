# -*- coding: utf-8 -*-

# Scrapy settings for shixisehng project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'shixisehng'

SPIDER_MODULES = ['shixisehng.spiders']
NEWSPIDER_MODULE = 'shixisehng.spiders'

#职位
LOCATION = '产品运营'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shixisehng (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

SCHEDULER="scrapy_redis.scheduler.Scheduler"

SCHEDULER_QUEUE_KEY="%(spider)s:requests"

DUPEFILTER_CLASS="scrapy_redis.dupefilter.RFPDupeFilter"

SCHEDULER_QUEUE_CLASS='scrapy_redis.queue.SpiderQueue'

# REDIS_URL = 'redis://:123456@192.168.0.47:6379'

REDIS_HOST = ''

REDIS_PORT = 6379

REDIS_PARAMS = {'db':0,'password':'123456'}

SCHEDULER_PERSIST=True

#异步请求个数

CONCURRENT_REQUESTS = 1

MYEXT_ENABLED=False # 开启扩展
#等待100s  没有任务自动关闭

IDLE_NUMBER= 0

EXTENSIONS = {'shixisehng.extensions.RedisSpiderSmartIdleClosedExensions': 500,
             }

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html


# SPIDER_MIDDLEWARES = {
#    'shixisehng.middlewares.ShixisehngSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'shixisehng.middlewares.ShixisehngDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
   'shixisehng.pipelines.MongoDBPipline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
