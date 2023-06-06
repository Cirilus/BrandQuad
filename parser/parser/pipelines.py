# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Item2Json:
    def process_item(self, item, spider):
        json_item = dict(item)
        with open(f"result/{item['RPC']}.json", "w") as file:
            json.dump(json_item, file, ensure_ascii=False)
        return item
