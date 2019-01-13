import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from doubanSpider.items import PageItem


class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    start_urls = ["http://flask.pocoo.org/docs/1.0/"]

    links = LinkExtractor(allow='http://flask.pocoo.org/docs/1.0/.*')

    rules = (
        Rule(link_extractor=links, callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        item = PageItem()
        item['url'] = response.url
        item['text'] = ''.join(response.xpath('//text()').extract())
        return item
