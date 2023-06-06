import json
import re

import scrapy
from ..items import ParserItem, PriceData, Stock, Assets, Metadata

class AptekaSpider(scrapy.Spider):
    name = "apteka"

    def __init__(self, *args, **kwargs):
        self.domain = "https://apteka-ot-sklada.ru"
        self.category = kwargs.get("category")

        self.count_product = 0
        self.step = 0
        self.ids = []

        self.url = f"{self.domain}/catalog/" + self.category + f"?start={self.count_product}"
        self.product_api = f"{self.domain}/api/catalog/"
        super().__init__(**kwargs)

    def start_requests(self):
        yield scrapy.Request(self.url, callback=self.parse_products)

    def parse_products(self, response, **kwargs):
        regex_pattern = r'(\d+)$'
        try:
            urls = response.css(".goods-card__link::attr(href)")
        except Exception as e:
            self.log(e)
            return
        self.step = len(urls)
        for url in urls:
            product_id = re.search(regex_pattern, url.get())[0]
            yield scrapy.Request(self.product_api + product_id, callback=self.parse_detail_product)

        self.count_product += self.step

        self.log(f"{self.count_product} was parsed")

        self.url = re.sub(r"(?<=start=)\d+", str(self.count_product), self.url)
        yield response.follow(self.url, callback=self.parse_products)

    def parse_detail_product(self, response, **kwargs):
        api_data = json.loads(response.text)
        item = ParserItem()
        price = PriceData()
        stock = Stock()
        assets = Assets()
        metadata = Metadata()

        price["current"] = api_data["cost"]
        price["original"] = api_data["startPrice"]

        stock["in_stock"] = bool(api_data["inStock"])
        stock["count"] = api_data["availability"]

        assets["main_image"] = api_data["images"][0]
        assets["set_image"] = api_data["images"][1:]

        metadata["description"] = api_data["description"]

        item["RPC"] = api_data["id"]
        item["url"] = self.domain + "/" + api_data["slug"]
        item["title"] = api_data["name"]
        item["brand"] = api_data["producer"]
        item["section"] = api_data["category"]["slug"].split("/")
        item["price_data"] = json.dumps(dict(price))
        item["stock"] = dict(stock)
        item["assets"] = dict(assets)
        item["metadata"] = dict(metadata)
        item["variants"] = 1

        yield item



