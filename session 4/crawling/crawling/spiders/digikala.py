import scrapy
import json
from crawling.items import DigiItem
class DigikalaSpider(scrapy.Spider):
    name = "digikala"
    allowed_domains = ["digikala.com"]
    
    def start_requests(self):
        for i in range(10):
            yield scrapy.Request('https://api.digikala.com/v1/categories/notebook-netbook-ultrabook/search/?sort=1&page={}'.format(i+1),
                                 callback=self.parse)

    def parse(self, response):
        content = response.text
        content = json.loads(content)
        for item in content['data']['products']:
            it = DigiItem()
            it.extract(item)
            yield it
