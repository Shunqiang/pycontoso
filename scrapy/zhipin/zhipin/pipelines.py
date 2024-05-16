# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ZhipinPipeline:
    def process_item(self, item, spider):
        print(item)
        print(122222)
        with open(file='全国-热门城市岗位数据.csv', mode='a+', encoding='utf8') as f:
            f.write(
                '{name},{time}\n'.format(
                    **item))
        return item
