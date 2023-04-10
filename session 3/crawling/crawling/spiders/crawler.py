import scrapy


class CrawlerSpider(scrapy.Spider):
    name = "crawler"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["http://wikipedia.org/"]

    def parse(self, response):
        pass
