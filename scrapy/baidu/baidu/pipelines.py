# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BaiduPipeline:
    def open_spider(self, spider):
        print(2222222)
    def process_item(self, item, spider):
        with open('book.json', 'w', encoding='utf-8') as fb:
            fb.write(str(item))
        return item
