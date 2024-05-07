# import scrapy
# import random
# import json
# from zhipin.items import ZhipinItem
# from selenium.webdriver.common.keys import Keys

# class BossZhipinSpider(scrapy.Spider):
#     name = "boss_zhipin"
#     allowed_domains = ["www.zhipin.com"]
#     start_urls = ["https://www.zhipin.com/wapi/zpgeek/search/joblist.json"]
#     base_url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json"
#     cookies = [
#         '__zp_stoken__=7ddffTVPDrsOZY8OKTkAgIB0gI05JTlM7IVFNR1NSTU1TUVRLTVNZMlk9ccORw7JaJm7DmsK7w5lMRlFSUU1TU1JSWDZRTsOYTVJGwpTDksOtWyJvw6kaWh56JVLDkh5zw5Iiw5zDkUZEwp3DmEpZUU7DlMOPwrnDjsOKw5XCqsOOw5XDi8K4w5VZWU5YRFUgHB9xVVlhaW8nZ3VoeXFbIGFjYEdOT1BSwoR5xJhGVCUaJB4lIxwiICMcIx0mHSQbJR8kIh0jISI6TcKuw4rCocS%2Fw6tsxJbEs8K4wqvDv8OAw4PCusKxbMOTecK3w5XCt8KIwqJmw4PDjcOQw4zCtcK%2BwrF2ZVvCu8KQbMORbcKNwoV0wr5pwoFhwpfDlsKLbcKSwocfa3RuKVUhw7d4w58%3D',
#         # '__zp_stoken__=f330bOEgsRnsAIU1dUCAZe250elQRdl89P2IQZ1hvW1JSe1NuCipKLWBtTU9iTAJ%2BPHtlVRgdTX5vZx8kSDwNZHY9InBRawJLKX8ESx5ac0cFI3kYKgskH1UEPX0WO2JEOipvRlwbP1YFBQlHOQ%3D%3D',
#         # '__zp_stoken__=f330bOEgsRnsAISRBIWtKe250elRwAXZ4fBEQZ1hvW2xPZBdzYipKLWBtE0xGIkV%2BPHtlVRgdTX51chckSi0jd1g6GW8vAAYpS31hX3ogc0cFI3kYKkxKO1ZaPX0WO2IsOipvRlwbP1YFBQlHOQ%3D%3D'
#         # '__zp_stoken__=f330bOEgsRnsAIVF5f10ce250elQIJnYiaigQZ1hvW29ScE1JWSpKLWBtAUNYRlh%2BPHtlVRgdTX51fRckLFRBFE1OBRhVeQYtcG5iRxEsc0cFI3kYKlEuJVlIPX0WO2IXOipvRlwbP1YFBQlHOQ%3D%3D'
#         # '__zp_stoken__=f330bOEgsRnsAIUgPQXkQe250elQRe3peYykQZ1hvW0V%2FKVskBCpKLWBtLAg3SDl%2BPHtlVRgdTX5xJkAkP146HCwDLxEucRknIgBtXBJUc0cFI3kYKjAgShJlPX0WO2JKOipvRlwbP1YFBQlHOQ%3D%3D'
#     ]
#     user_agents = [
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
#         'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
#         'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#         'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
#         'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
#         'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
#         'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
#         'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
#     ]
#     page_no = 1  # 初始化分页

#     def random_headers(self):
#         # 随机生成请求头
#         headers = {'Referer': 'https://www.zhipin.com/web/geek/job?query=&city=101020100&position=150203'}
#         headers['cookie'] = random.choice(self.cookies)
#         headers['user-agent'] = random.choice(self.user_agents)

#     def parse(self, response):
#         print('--------------------------')
#         url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101020100&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=150203&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30'
#         yield response.follow(url, headers=self.random_headers(),callback=self.formatTime)
#     def formatTime(self, response):
#         item = ZhipinItem(name = 1, time = 2)
#         print('22222222222222')
#         print(response.body)
#         with open('tst.json', 'w', encoding='utf-8') as fb:
#             fb.write(str(response.body))
#         yield item


import scrapy
import json
import logging
import random
from zhipin.items import ZhipinItem


class BossSpider(scrapy.Spider):
    name = 'boss_zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/wapi/zpCommon/data/cityGroup.json']
    # 设置多个 cookie,建议数量为 页数/2 + 1 个cookie.至少 设置 3 个
    cookies = [
        '__zp_stoken__=3ac4fO0fDpMOFScK4QjYcHR4SFk43REcpJEA7K0E6QztHRzhBO0dPGkcrEsOHKMO%2BE2LDiMKLw4c6Kkc6TztHQTo4ThpHTsOGO0Y8KMK4KcOxH2%2FDlwgIFEXCuAgIw4c0wrDCuxRswro1KUDDhkVHTDjDhMK4wqfDjxnDhcKlw4wyw4XDk8K5R0TChD8%2FOx0WE1o7REtJWBVWb0hib1IKUVxeNjhDOzhpY8O4MToIFBQJCx8TEx4cHxMTCwkKFhYLCQsXFwoIM0fCocOFSHvGh0vEgcSZwqXDh8KVX8OrwrnCkXzDu3%2FDu27EhMKzwrdiwr7CqsKiwrhRwrLCq3bConHCo8Kqc8OEZ2dywoJ1w49aUsODEHtJWBIdHG9lHjscwpErw4k%3D',
    ]
    # 设置多个请求头
    user_agents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    ]
    page_no = 1  # 初始化分页

    def random_header(self):
        """
        随机生成请求头
        :return: headers
        """
        headers = {'Referer': 'https://www.zhipin.com/c101020100/?ka=sel-city-101020100'}
        headers['cookie'] = random.choice(self.cookies)
        headers['user-agent'] = random.choice(self.user_agents)
        return headers

    def parse(self, response):
        """
        解析首页热门城市列表，选择热门城市进行爬取
        :param response: 热门城市字典数据
        :return:
        """
        # 获取服务器返回的内容
        city_group = json.loads(response.body.decode())
        # 获取热门城市列表
        hot_city_list = city_group['zpData']['hotCityList']
        # 初始化空列表，存储打印信息
        # city_lst = []
        # for index,item in enumerate(hot_city_list):
        #    city_lst.apend({index+1: item['name']})
        # 列表推导式：
        hot_city_names = [{index + 1: item['name']} for index, item in enumerate(hot_city_list)]
        print("--->", hot_city_names)
        # 从键盘获取城市编号
        city_no = int(input('请从上述城市列表中，选择编号开始爬取：'))
        # 拼接url https://www.zhipin.com/job_detail/?query=&city=101040100&industry=&position=
        # 获取城市编码code
        city_code = hot_city_list[city_no - 1]['code']
        city_url = 'https://www.zhipin.com/job_detail/?query=&city=101020100&industry=&position='.format(city_code)
        logging.info("<<<<<<<<<<<<<正在爬取第_{}_页岗位数据>>>>>>>>>>>>>".format(self.page_no))
        yield scrapy.Request(url=city_url, headers=self.random_header(), callback=self.parse_city)

    def parse_city(self, response):

        """
        解析岗位页数据
        :param response: 岗位页响应数据
        :return:
        """

       
        if response.status != 200:
            logging.warning("<<<<<<<<<<<<<获取城市招聘信息失败，ip已被封禁。请稍后重试>>>>>>>>>>>>>")
            return
        li_elements = response.xpath('//div[@class="job-list"]/ul/li')  # 定位到所有的li标签
        next_url = response.xpath('//div[@class="page"]/a[last()]/@href').get()  # 获取下一页
        print(11111)
        print(response.text)
        print(li_elements)
        for li in li_elements:
            job_name = li.xpath('./div/div[1]//div[@class="job-title"]/span[1]/a/text()').get()
            job_area = li.xpath('./div/div[1]//div[@class="job-title"]/span[2]/span[1]/text()').get()
            job_salary = li.xpath('./div/div[1]//span[@class="red"]/text()').get()
            com_name = li.xpath('./div/div[1]/div[2]//div[@class="company-text"]/h3/a/text()').get()
            com_type = li.xpath('./div/div[1]/div[2]/div[1]/p/a/text()').get()
            com_size = li.xpath('./div/div[1]/div[2]/div[1]/p/text()[2]').get()
            finance_stage = li.xpath('./div/div[1]/div[2]/div[1]/p/text()[1]').get()
            work_year = li.xpath('./div/div[1]/div[1]/div[1]/div[2]/p/text()[1]').get()
            education = li.xpath('./div/div[1]/div[1]/div[1]/div[2]/p/text()[2]').get()
            job_benefits = li.xpath('./div/div[2]/div[2]/text()').get()
            item = ZhipinItem(name=job_name, time=job_area)
            
            yield item
        if next_url == "javascript:;":
            logging.info('<<<<<<<<<<<<<热门城市岗位数据已爬取结束>>>>>>>>>>>>>')
            logging.info("<<<<<<<<<<<<<一共爬取了_{}_页岗位数据>>>>>>>>>>>>>".format(self.page_no))
            return
        next_url = response.urljoin(next_url)  # 网址拼接
        self.page_no += 1
        logging.info("<<<<<<<<<<<<<正在爬取第_{}_页岗位数据>>>>>>>>>>>>>".format(self.page_no))
        yield scrapy.Request(url=next_url, headers=self.random_header(), callback=self.parse_city)
