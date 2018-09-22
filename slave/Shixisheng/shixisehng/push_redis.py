#coding:utf-8

from redis import Redis

def push_redis():
    r = Redis(host='',port=6379,password='123456')

    url = r.brpoplpush('master:start_urls','slave:urls',3)
    
    return url