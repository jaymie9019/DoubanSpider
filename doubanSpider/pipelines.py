# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

import redis
import json
from scrapy.exceptions import DropItem


class DoubanspiderPipeline(object):
    def process_item(self, item, spider):
        if item['score'] < 8.0:
            raise DropItem('score less than 8')
        else:
            self.redis.lpush('douban_movie:items', json.dumps(dict(item)))

        return item

    def open_spider(self, spider):
        self.redis = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)


class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        item['text'] = re.sub(r'\s+', '', item['text'])
        self.redis.lpush('flask_doc:items', json.dumps(dict(item)))
        return item

    def open_spider(self, spider):
        # 连接数据库
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
