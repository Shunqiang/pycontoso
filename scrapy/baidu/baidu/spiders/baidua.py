import scrapy


class BaiduaSpider(scrapy.Spider):
    name = "baidua"
    allowed_domains = ["https://www.zhipin.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job-recommend?ka=open_joblist"]

    def parse(self, response):
        print(response.body.decode('utf8'))
        # text =response.xpath('//div[@id="u1"]')
        yield {
                "text":response.xpath("//title/text()").get(),
            }
        pass
