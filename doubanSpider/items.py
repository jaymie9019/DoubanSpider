# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    summary = scrapy.Field()
    score = scrapy.Field()


class PageItem(scrapy.Item):
    url = scrapy.Field()
    text = scrapy.Field()
