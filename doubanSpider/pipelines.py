# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
r = redis.StrictRedis(host='127.0.0.1', db=0)


class DoubanspiderPipeline(object):
    def process_item(self, item, spider):
        if item['score'] >= 8:
            r.rpush('douban_movie:items', str(item))

        return item
