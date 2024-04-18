import scrapy
from baidu.items import BaiduItem

class BaiduaSpider(scrapy.Spider):
    name = "baidua"
    # allowed_domains = ["https://bj.58.com"]
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        # print(response.body.decode('utf8'))
        # text =response.xpath('//div[@id="u1"]')
        # print(response.text)
        # print(123333)
        next_page = response.css("li.next a::attr(href)").get()
        book = BaiduItem(name=next_page, src=11)
        # print('22233333333333333333333')
        yield book
        # for href in response.css("ul.pager a::attr(href)"):
        #     yield response.follow(href, callback=self.parse)
        # pass
