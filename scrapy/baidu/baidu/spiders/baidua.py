import scrapy


class BaiduaSpider(scrapy.Spider):
    name = "baidua"
    allowed_domains = ["https://bj.58.com"]
    start_urls = ["https://www.58.com/fangdichan/?PGTID=0d002408-0000-052d-7d50-af041bfbf6e3&ClickID=1"]

    def parse(self, response):
        print(response.body.decode('utf8'))
        # text =response.xpath('//div[@id="u1"]')
        print(text)
        pass
