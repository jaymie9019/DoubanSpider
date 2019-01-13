# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from doubanSpider.items import MovieItem


class AwesomeMovieSpider(CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']

    links = LinkExtractor(restrict_xpaths='//div[@class="recommendations-bd"]/dl//a')


    rules = (
        Rule(link_extractor=links, callback="parse_page", follow=True),
    )

    def parse_movie_item(self, response):
        item = MovieItem()
        item['name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract_first().strip()
        item['url'] = response.url
        item['summary'] = response.xpath('//span[@property="v:summary"]/text()').extract_first().strip()
        item['score'] = float(response.xpath('//strong[@property="v:average"]/text()').extract_first().strip())
        return item

    def parse_start_url(self, response):
        yield self.parse_movie_item(response)

    def parse_page(self, response):
        yield self.parse_movie_item(response)
