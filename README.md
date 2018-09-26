# Shixisheng
环境：Python3.6
分布式 scrapy_redis去重 + MongoDB 持久化数据 + Bloom 布隆去重

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

py_bloomfilter 为布隆去重源码 接下来需要对接scrapy_redis 进行去重

相比于其它的数据结构，布隆过滤器在空间和时间方面都有巨大的优势。布隆过滤器存储空间和插入/查询时间都是常数。另外, Hash 函数相互之间没有关系，方便由硬件并行实现。布隆过滤器不需要存储元素本身，在某些对保密要求非常严格的场合有优势。

布隆过滤器可以表示全集，其它任何数据结构都不能；

但是布隆过滤器的缺点和优点一样明显。误算率（False Positive）是其中之一。随着存入的元素数量增加，误算率随之增加。但是如果元素数量太少，则使用散列表足矣。

另外，一般情况下不能从布隆过滤器中删除元素. 我们很容易想到把位列阵变成整数数组，每插入一个元素相应的计数器加1, 这样删除元素时将计数器减掉就可以了。然而要保证安全的删除元素并非如此简单。首先我们必须保证删除的元素的确在布隆过滤器里面. 这一点单凭这个过滤器是无法保证的。另外计数器回绕也会造成问题。

dupefilter.py（这个为scrapy_redis里的去重源码，已修改过），scrapy_redis 版本:V0.6.8  可以替换这个文件，直接进行对接，经测试效果良好，由于个人机器性能有限，第二次请求进行过滤去重 总被卡死（内存吃紧），大家玩的时候需要注意一下。。。






