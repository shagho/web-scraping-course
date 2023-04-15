import scrapy


class CrawlerSpider(scrapy.Spider):
    name = "crawler"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://fa.wikipedia.org/wiki/%D8%B1%D8%AF%D9%87:%D8%AF%D8%A7%D9%86%D8%B4%D9%85%D9%86%D8%AF%D8%A7%D9%86_%D8%B1%D8%A7%DB%8C%D8%A7%D9%86%D9%87"]

    def parse(self, response):
        items = response.xpath('//div[@id="mw-pages"]/div[@class="mw-content-rtl"]/div[@class="mw-category mw-category-columns"]/div[@class="mw-category-group"]/ul/li/a/@href').extract()

        for item in items:
            yield scrapy.Request('https://fa.wikipedia.org' + item, callback=self.sub_page, cb_kwargs={"page": 2})

    def sub_page(self, response, page=1):
        contents = response.xpath('//div[@class="mw-parser-output"]/p')
        for item in contents:
            variable = ' '.join(item.xpath('text()').extract())
            if variable.strip() != "":
                yield {"intro": variable}
                break
