# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import datetime

import scrapy


class PriceData(scrapy.Item):
    current = scrapy.Field()
    original = scrapy.Field()
    sale_rag = scrapy.Field()


class Stock(scrapy.Item):
    in_stock = scrapy.Field()
    count = scrapy.Field()


class Assets(scrapy.Item):
    main_image = scrapy.Field()
    set_image = scrapy.Field()
    view360 = scrapy.Field()
    video = scrapy.Field()


class Metadata(scrapy.Item):
    description = scrapy.Field()


class ParserItem(scrapy.Item):
    timestamp = scrapy.Field()
    RPC = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    marketing_tags = scrapy.Field()
    brand = scrapy.Field()
    section = scrapy.Field()
    price_data = scrapy.Field()
    stock = scrapy.Field()
    assets = scrapy.Field()
    metadata = scrapy.Field()
    variants = scrapy.Field()
