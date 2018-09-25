# Shixisheng
分布式 scrapy_redis去重 + MongoDB 持久化数据

先运行 cd master 主负责丢链接到队列

python3 run.py  


然后进入 slave

运行 python3 run.py

也可以设置无人值守 

建立crontab 计划任务  执行start.sh 脚本。。。


扩展：

防止spider 执行完以后，空跑， 我利用的是超时控制的 CLOSESPIDER_TIMEOUT=600 （单位秒/S） ，

当spider 执行完后等待600S 后没有新的request时，爬虫则自动关闭

以下是可选参数：

$ scrapy crawl master -s CLOSESPIDER_ITEMCOUNT=10
$ scrapy crawl master -s CLOSESPIDER_PAGECOUNT=10
$ scrapy crawl master -s CLOSESPIDER_TIMEOUT=10

---------------------

